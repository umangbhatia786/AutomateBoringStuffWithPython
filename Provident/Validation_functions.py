import xml.etree.ElementTree as et
import re
import logging

def INF_Validation(request_content,svas_content):
	logger = logging.getLogger()
	logger.info("Starting INF Validation")
	inf_a_pattern_request = r"INF_a { n!OPT=[A-Z&+=&0-9]+ }"
	inf_a_pattern_svas = r'"INF_a",{n,"OPT=[A-Z&+=&0-9]+"}'
	search_pattern = r"OPT=[A-Z&+=0-9]+"
	
	if re.search(inf_a_pattern_request, request_content):
		content_req = re.findall(inf_a_pattern_request, request_content)[0]
		search_text_req = re.findall(search_pattern,content_req)[0]
        
		content_svas = re.findall(inf_a_pattern_svas, svas_content)[0]
		search_text_svas = re.findall(search_pattern,content_svas)[0]

        #print(search_text_req)
        #print(search_text_svas)
		if search_text_req == search_text_svas:
			logger.info("SVAS validation for INF_a Passed")  
		else:
			logger.error("SVAS validation for INF_a Failed")

def HOLD_Validation(request_content,svas_content,hss_content):
	logger = logging.getLogger()
	logger.info("Starting validation for HOLD_a")  
	if("HOLD_a" in svas_content):
		logger.info("SVAS validation for HOLD_a Passed")  
	else:
		logger.error("SVAS validation for HOLD_a Failed")  

	if(r'<hold>true</hold>' in hss_content):
		logger.info("HSS validation for HOLD_a Passed")
	else:
		logger.error("HSS validation for HOLD_a Failed") 
