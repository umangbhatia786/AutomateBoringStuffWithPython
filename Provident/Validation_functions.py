import xml.etree.ElementTree as et
import re
import logging

#Dictionaries for search patterns in Request and Log files

request_pattern_dict = {
	"INF" : r"INF_a { n!OPT=[A-Z&+=&0-9]+ }"
	"CAW" : r"CAW_a { t!SW=[0-1]+ }"
}

svas_pattern_dict = {
	"INF" : r'"INF_a",{n,"OPT=[A-Z&+=&0-9]+"}',
	"CAW" : r'CAW_a",{t,"SW=[0-1]+"}'
}


search_pattern_dict = {
	"INF" : r"OPT=[A-Z&+=0-9]+"
	"CAW" : r"SW=[0-1]+"
}

#Method to return content desired content from svas logs and request file
def vaildateSVASLog(request_content, svas_content, request_pattern, svas_pattern, search_pattern):

	NAC_request_pattern = request_pattern
	svas_request_pattern = svas_pattern
	common_search_pattern = search_pattern
	
def INF_Validation(request_content,svas_content):
	logger = logging.getLogger()
	logger.info("Starting INF_a Validation.....")
	inf_a_pattern_request = r"INF_a { n!OPT=[A-Z&+=&0-9]+ }"
	inf_a_pattern_svas = r'"INF_a",{n,"OPT=[A-Z&+=&0-9]+"}'
	search_pattern = r"OPT=[A-Z&+=0-9]+"
	
	if re.search(inf_a_pattern_request, request_content):
		content_req = re.findall(inf_a_pattern_request, request_content)[0]
		search_text_req = re.findall(search_pattern,content_req)[0]
        
		content_svas = re.findall(inf_a_pattern_svas, svas_content)[0]
		search_text_svas = re.findall(search_pattern,content_svas)[0]

		if search_text_req == search_text_svas:
			logger.info("SVAS validation for INF_a Passed. Both Request and SVAS Log contain " + search_text_req + " in OPT")  
		else:
			logger.error("SVAS validation for INF_a Failed. Expected: " + search_text_req + " Actual: " + search_text_svas)

def HOLD_Validation(request_content,svas_content,hss_content):
	logger = logging.getLogger()
	logger.info("Starting validation for HOLD_a...")  
	if("HOLD_a" in svas_content):
		logger.info("SVAS validation for HOLD_a Passed. SVAS Log contains HOLD_a attribute")  
	else:
		logger.error("SVAS validation for HOLD_a Failed. SVAS Log does not contain HOLD_a attribute")  

	if(r'<hold>true</hold>' in hss_content):
		logger.info("HSS validation for HOLD_a Passed. <hold> tag is true in HSS Logs")
	else:
		logger.error("HSS validation for HOLD_a Failed. <hold> tag is missing or not True in the HSS Logs") 

def CAW_Validation(request_content,svas_content,hss_content):
	logger = logging.getLogger()
	logger.info("Starting Call Waiting Validations...")
	caw_a_pattern_request = r"CAW_a { t!SW=[0-1]+ }"
	caw_a_pattern_svas = r'CAW_a",{t,"SW=[0-1]+"}'
	search_pattern = r"SW=[0-1]+"

	if re.search(caw_a_pattern_request, request_content):
		content_req = re.findall(caw_a_pattern_request, request_content)[0]
		search_text_req = re.findall(search_pattern,content_req)[0]
        
		content_svas = re.findall(caw_a_pattern_svas, svas_content)[0]
		search_text_svas = re.findall(search_pattern,content_svas)[0]

		if search_text_req == search_text_svas:
			logger.info("SVAS validation for CAW_a Passed. SW Setting is " + search_text_req + " for both request and SVAS Log")  
		else:
			logger.error("SVAS validation for CAW_a Failed. Expected: " + search_text_req + " Actual: " + search_text_svas)

	if(search_text_req == 'SW=1'):
		if(r'<basicServiceGroup>TS10-telephony</basicServiceGroup>' in hss_content and '<status>5</status>' in hss_content):
			logger.info("HSS Validation for CAW_a Passed for SW = 1 with <status> as 5")

		else:
			logger.info("HSS Validation for CAW_a Failed for SW = 1 with <status> not equal to 5")

	elif(search_text_req == 'SW=0'):
		if(r'<basicServiceGroup>TS10-telephony</basicServiceGroup>' in hss_content and '<status>4</status>' in hss_content):
			logger.info("HSS Validation for CAW_a Passed for SW = 0 with <status> as 4")

		else:
			logger.info("HSS Validation for CAW_a Failed for SW = 0 with <status> not 4")









