'''
Created on 21 Feb 2020

@author: 611841191
'''
from main.fileReader import readFile
import re

request_file_path = r"C:\Users\611841191\Documents\Request_and_Logs\New Activation.txt"
request_content = readFile(request_file_path)
#print(request_content)

svas_path = r"C:\Users\611841191\Documents\Request_and_Logs\SVAS.txt"
svas_content = readFile(svas_path)
#print(svas_content)

inf_a_pattern = r"INF_a { n!OPT=[A-Z&+=&0-9]+ }"
search_pattern = r"OPT=[A-Z&+=0-9]+"

if re.search(inf_a_pattern, request_content):
    content = re.findall(inf_a_pattern, request_content)[0]
    search_text = re.findall(search_pattern,content)[0]
    
    print(content)
    print(search_text)
    
    if search_text in svas_content:
        print("Validation passed")
        
    else:
        print("Validation Failed")
