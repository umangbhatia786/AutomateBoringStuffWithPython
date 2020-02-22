import xml.etree.ElementTree as et
import re
from fileReader import readFile
import logging
from Validation_functions import *

logging.basicConfig(filename="validation_logs.log",level=logging.DEBUG,format='%(levelname)s %(asctime)s %(message)s',filemode='w')

logger = logging.getLogger()
logger.info("Loding Config File")
config_file = et.ElementTree(file='config.xml')
config_root = config_file.getroot()

logger.info("Identifying Path Node of Request and Log Files")
request_file_path = config_root.find('NAC').find('RequestFile').find('Path').text
logFiles = config_root.find('NAC').findall('LogFile')

svas_log_path = ""
hss_log_path = ""
for logFile in logFiles:
    if(logFile.attrib['type'] == 'SVAS'):
        svas_log_path = logFile.find('Path').text
    if(logFile.attrib['type'] == 'HSS'):
        hss_log_path = logFile.find('Path').text

logger.info("Reading content from indentified files")
request_content = readFile(request_file_path)
svas_content = readFile(svas_log_path)
hss_content = readFile(hss_log_path)

if("INF_a" in request_content):
    INF_Validation(request_content,svas_content)
    
if("HOLD_a" in request_content):
    HOLD_Validation(request_content,svas_content,hss_content)
