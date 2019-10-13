'''
Created on Oct 13, 2019

@author: Umang Bhatia
'''

#! python3
# an insecure password manager
import sys, pyperclip
password_dict = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv)<2 :
    print('Uasge python pw.py [account] - copy account password')
    sys.exit()
    
account = sys.argv[1]

if account in password_dict:
    pyperclip.copy(password_dict[account])
    print('Password for ' + account + ' copied to clipboard')
    
else:
    print('There is no account named ' + account)
    
    
