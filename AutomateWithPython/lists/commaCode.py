'''
Created on Oct 12, 2019

@author: Umang Bhatia
'''

def formattedString(inputList):
    outputString = ''
    for i in range(len(inputList)):
        if i == len(inputList) - 1:
            outputString += 'and ' + str(inputList[i])
        else:
            outputString += str(inputList[i]) + ', '
            
    return outputString

def header():
    print('****************************************************')
    print('****** Welcome to the Comma Formatter Program ******')
    print('****************************************************')
    
def output(givenList):
    print()
    print('****** Your formatted string is ******')
    print(formattedString(givenList))
    

header()

sampleList = []

while True:
    inputVal = input('Enter list element / Press Enter to stop:')
    if inputVal == '':
        break
    else:
        sampleList.append(inputVal)
        
output(sampleList)