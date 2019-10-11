'''
Created on Oct 11, 2019

@author: Umang Bhatia
'''

#This is a sample program to create number guess game
import random

def gameHeader():
    print('**********************************************************')
    print('************ Welcome to the Number Guess Game ************')
    print('**********************************************************')

gameHeader()

secretNumber = random.randint(1,10)
print()
print('I am thinking of a secret number between 1 and 10')

count = 1

while True:
    chosenNumber = int(input('Make a guess: '))
    
    if chosenNumber == secretNumber:
        if count == 1:
            print('You made the correct choice in ' + str(count) + ' guesse')
        else:
            print('You made the correct choice in ' + str(count) + ' guesses')
        break
    else:
        count +=1
        continue




