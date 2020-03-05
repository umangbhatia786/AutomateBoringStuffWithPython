import PySimpleGUI as sg 
import psutil
from Validator import *


sg.theme('Light Blue 2')

layout = [[sg.Text('Choose files to get started', size=(30, 1), justification='center', font=("Helvetica", 25), relief=sg.RELIEF_RIDGE)],
          [sg.Text('Request File', size=(15,1)), sg.Input(key='req'), sg.FileBrowse()],
          [sg.Text('SVAS Log File', size=(15,1)), sg.Input(key='svas'), sg.FileBrowse()],
          [sg.Text('HSS Log File', size=(15,1)), sg.Input(key='hss'), sg.FileBrowse()],
          [sg.Submit('Generate Logs'), sg.Cancel('Quit'), sg.Button('Reset')]]


window = sg.Window('Provident Logs Validator', layout, size=(600,300))

while True:
    event, values = window.read()
  
    if event in (None, 'Quit'):
        window.close()
        for proc in psutil.process_iter():
            if proc.name() == 'ValidatorGUI.exe':
                proc.kill()
                
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
