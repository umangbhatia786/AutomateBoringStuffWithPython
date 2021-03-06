import PySimpleGUI as sg
from validator import *

def print1():
    print('Generate Logs Clicked')

def print2():
    print('Quit Clicked')


sg.theme('Light Blue 2')

layout = [[sg.Text('Choose files to get started', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
          [sg.Text('Request File', size=(15,1)), sg.Input(key='req'), sg.FileBrowse()],
          [sg.Text('SVAS Log File', size=(15,1)), sg.Input(key='svas'), sg.FileBrowse()],
          [sg.Text('HSS Log File', size=(15,1)), sg.Input(key='hss'), sg.FileBrowse()],
          [sg.Submit('Generate Logs'), sg.Cancel('Quit'), sg.Button('Reset')],
          [sg.Txt('', size=(8,1), key='output')]]

window = sg.Window('Provident Logs Validator', layout, size=(800,200))

event, values = window.read()
'''window.close()
print(f'You clicked {event}')
print(f'You chose filenames {values[0]} and {values[1]}')'''



while True:
    event, values = window.read()
    if event in (None, 'Quit'):
        window.close()
    elif event == 'Generate Logs':
        try:
            validator(values)
            sg.popup('Logs Generated Succesfully!!')
        except Exception as e:
            sg.popup("Error - Select all the files again")
        finally:
            window['req']('')
            window['svas']('')
            window['hss']('')
            values = {}

    elif event == 'Reset':
        window['req']('')
        window['svas']('')
        window['hss']('')
        values = {}
