import re

''' Function to read data from a txt file '''

def readFile(filePath):
    
    input_file = open(filePath, "r")
    
    if input_file.mode == "r":
        file_content = input_file.read()
        
    input_file.close()
    
    return file_content

''' Function to read and find data for a particular tag pattern inside an xml '''

def findTags(xmlPath, tagPattern):
    
    xml_content = readFile(xmlPath)
    tagContentList = re.findall(tagPattern, xml_content)
    
    return tagContentList
        
    
