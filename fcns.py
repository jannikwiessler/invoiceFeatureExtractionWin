#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 17:19:26 2019

@author: jannik wiessler
"""
import re
import os
#from os.path import join
from pandas import DataFrame
#from fcn_logging import autolog
#import pdftotext_input
import tesseract4
#import tesseract4windows
#from pytesseract import image_to_string
import logging

# =============================================================================
# from .input import pdfminer_wrapper
# from .input import tesseract
# from .input import tesseract4
# from .input import gvision
# =============================================================================


# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-01
# descrip:  fcn to extract data from pdf
# =============================================================================
def extract_mydata_pdf(invoicefile, input_module=tesseract4):
    logging.debug('extract_mydata_pdf: start extract data to string')
    extracted_str = input_module.to_text(invoicefile).decode('utf-8')
#    extracted_str = image_to_string(invoicefile).decode('utf-8')
    extracted_str = extracted_str.replace('—','-')
    logging.debug('extract_mydata_pdf: extracting complete')
    return extracted_str

# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-08
# descrip:  fcn to find all keywords in template:
#           '\n' is one char, eg: template[10] = '\n'   
# info:     caller must not use "'" within a keywords name    
# =============================================================================
def get_keywords(template):
    str2find = 'keywords:'
    keywords = []
    loop = 1
    idx_start = template.find(str2find)
    if idx_start == -1:
        logging.debug('get_keywords: keywords in template not found')
        return
    
    idx_linebreak = template.find('\n',idx_start+len(str2find)) # get first linebreak
    while loop == 1:
        if template[idx_linebreak+1] == '-':
            idx_str_start = template.find("'",idx_linebreak)
            idx_str_end   = template.find("'",idx_str_start+1)
            idx_linebreak = template.find('\n',idx_str_end)
            keywords.append(template[idx_str_start+1:idx_str_end])
        else:
            loop = 0

    return keywords

# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-09
# descrip:  fcn get issuer from template
# =============================================================================  
def get_issuer2(template):    
    str2find = 'issuer:'
    issuer = []
    loop = 1
    idx_start = template.find(str2find)
    if idx_start == -1:
        logging.debug('get_issuer2: issuer in template not found')
        return
    
    idx_linebreak = template.find('\n',idx_start+len(str2find)) # get first linebreak
    while loop == 1:
        if template[idx_linebreak+1] == '-':
            idx_str_start = template.find("'",idx_linebreak)
            idx_str_end   = template.find("'",idx_str_start+1)
            idx_linebreak = template.find('\n',idx_str_end)
            issuer.append(template[idx_str_start+1:idx_str_end])
        else:
            loop = 0

    return issuer
    
# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-09
# descrip:  fcn get fields from template
# =============================================================================  
def get_fields(template,invoice,field_dic):
    str2find = 'fields:'

    dic = {}
    for value in field_dic.values(): # initialize empty dic
        dic[value] = None
        
    loop = 1
    idx_start = template.find(str2find)
    if idx_start == -1:
        logging.debug('get_fields: fields in template not found')
        return
    
    idx_linebreak = template.find('\n',idx_start+len(str2find)) # get first linebreak
    while loop == 1:
        if template[idx_linebreak+1] == '-':
            idx1_str_start = template.find("",idx_linebreak)
            idx1_str_end   = template.find(":",idx1_str_start+1)
            idx2_str_start = template.find("'",idx1_str_end)
            idx2_str_end   = template.find("'",idx2_str_start+1)
            idx_linebreak  = template.find('\n',idx2_str_end)
            
            string = template[idx1_str_start:idx1_str_end]
            temp = template[idx2_str_start+1:idx2_str_end]
            res_find = re.findall(temp, invoice)
            
            for field in field_dic:
                if field_dic[field] in string:
                    dic[field_dic[field]] = res_find

        else:
            loop = 0

    return dic
         
    
    
# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-08
# descrip:  fcn to find corresponding template
# update:   2019-12-13: added try catch statement for not openable data (./DSstore)
# =============================================================================
def get_invoicedata(invoice,templatefolder,field_dic):
    templates = os.listdir(templatefolder)
    for j in range(len(templates)): # get template
        try:
            file = open(templatefolder+templates[j],encoding="utf8",mode='r') # open current template
            template = file.read()
            file.close() # closecurrent template    
        except: 
            file = 0
        if file:
            temp = [] 
            keywords = get_keywords(template)    
            for i in range(len(keywords)):
                if invoice.find(keywords[i]) != -1:
                    temp.append(invoice.find(keywords[i]))    
            if len(temp) >= 0.8*len(keywords): # check if template is found then extract data
                issuer = get_issuer2(template)  
                fields = get_fields(template,invoice,field_dic)
                out = fields # rename
                out['issuer'] = issuer
                out['template'] = [templates[j]]
                return out
        else:
            logging.debug('get_invoicedata: can not open template: '+templates[j])
        
# =============================================================================
# autor:    jannik wiessler
# date:     2019-08-11
# descrip:  add new data to dataframe for wirting into excel
# =============================================================================
def add_todataframe(df,excel_dic,data):  
    temp = {}
    for i in range(len(df.columns)):
        if bool(data[excel_dic[df.columns[i]]]): # if is not empty
            temp[df.columns[i]] = data[excel_dic[df.columns[i]]]
        else: # if is empty put -1 in dictionary
            temp[df.columns[i]] = -1

                
    
    return df.append(DataFrame(temp))