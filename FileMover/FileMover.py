import shutil
import os

#Defined Paths for Source and Destination Folders
source = r'C:/Users/Umang Bhatia/Documents/File_Arrange/'
pass_folder = r'C:/Users/Umang Bhatia/Documents/File_Arrange/Passed'
fail_folder = r'C:/Users/Umang Bhatia/Documents/File_Arrange/Failed'

#Listing all the Files and Folders inside the Source Path Directory
files = os.listdir(source)

#Looping through File Names and Moving them accordingly

for file in files:
    #shutil.move(source+f, dest1)
    if '.txt' in file and 'FAIL' in file:
       shutil.move('{}{}'.format(source,file), fail_folder)
    
    elif '.txt' in file and 'OK' in file:
       shutil.move('{}{}'.format(source,file), pass_folder)
