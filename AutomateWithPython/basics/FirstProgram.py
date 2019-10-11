'''
Created on Oct 11, 2019

@author: Umang Bhatia
'''

#This program says hello and asks for my name and age

print('************************************')
print('Hello, Hope you\'re well')
print('Welcome to your first python program')
print('************************************')
print()

myName = input('What is your name? : ')
print('Nice meeting you ' + myName)
print('The length of your name is ' + str(len(myName)))
myAge = int(input('What is your age? : '))
print('You will be ' + str(myAge + 1) + ' in an year')

