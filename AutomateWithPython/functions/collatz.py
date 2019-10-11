'''
Created on Oct 11, 2019

@author: Umang Bhatia
'''

#This is a sample program to create a function that prints collatz sequence for any number

def collatz(number):
    if number % 2 == 0:
        return number//2
    else:
        return 3* number + 1
    
def progHeader():
    print('***********************************************************************')
    print('************** Welcome to Collatz Sequence Program*********************')
    print('***********************************************************************')
    print()

progHeader()
    
num = int(input('Enter a number: '))
print()
print('******* Your Collatz Numbers are *************')

count = num
while count!=1:
    count = collatz(count)
    print(count)
    
print('**********************************************')