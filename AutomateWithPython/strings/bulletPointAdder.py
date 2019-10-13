'''
Created on Oct 13, 2019

@author: Umang Bhatia
'''

# adds Wikipedia bullet point to each line of copied text

import pyperclip

text = pyperclip.paste()

# Add seperate lines and stars
lines = text.split('\n')

for i in range(len(lines)):
    if not lines[i].isspace():
        lines[i] = '* ' + lines[i]
    
text = '\n'.join(lines)

pyperclip.copy(text)