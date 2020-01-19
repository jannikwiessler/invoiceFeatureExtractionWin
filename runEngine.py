#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 14:08:44 2019

@author: jannik
"""
# Notice:
# >>os.path.dirname<< return empty string if script is executed but works by calling the executable
# workaround: os.path.abspath(__file__)
# __file__ is full abs path
# os.path.basename(__file__) is script name with .py
# -1 for last backslash which is not returned by dirname

from engine_preprocess import engine_preprocess
from engine_main import engine_main
import os
import sys
import logging
import time

progressCounter = 0

print(progressCounter)
time.sleep(0.01)
# get current directory: specs must be in same folder !
if getattr(sys, 'frozen', False): 
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.abspath(__file__)
    application_path = application_path[0:-(len(os.path.basename(__file__))+1)]

logging.basicConfig(filename=application_path+'/runEngineInfo.log',
                    level=logging.DEBUG,
                    format='%(asctime)-15s %(name)s %(message)s')
logging.debug('runEngine: engine started successfully')

# script to start the invoice expanding engine
keywords = ['invoice_path','invoice_name','destination_path']  # keywords from txt file to read infos from gui
idx = {} # dictionary for line idx
temp = {} 
with open(application_path+'/invoice_Path.txt','r') as f:
    data = f.readlines()
logging.debug('runEngine: reading invoice_Path.txt completed')

# sorting invoicepath, invoicename, destinationpath
for i, keyword in enumerate(keywords): # loop over keywords
    for j in range(len(data)): # loop over lines
        if data[j].find(keywords[i]) != -1:
            idx[keyword] = j            
idx = sorted(idx.items(), key=lambda item: item[1])     
for i in range(len(idx)-1): # loop over idx
    for j in range(len(keywords)):
        if idx[i][0] == keywords[j]:
            temp[keywords[j]] = data[idx[i][1]+1:idx[i+1][1]]
i = len(idx)-1 # last entry
for j in range(len(keywords)):
        if idx[i][0] == keywords[j]:
            temp[keywords[j]] = data[idx[i][1]+1:]

# cutting string if it end on '\n'
for i, keyword in enumerate(keywords): 
    for j in range(len(temp[keyword])):
        if temp[keyword][j][-1] == '\n': # string ends with '\n'
            temp[keyword][j] = temp[keyword][j][:len(temp[keyword][j])-1]
logging.debug('runEngine: sorting invoicepath, invoicename, destinationpath completed')  

# starting the engine
progressCounter = progressCounter + 2
print(progressCounter)
time.sleep(0.01)
logging.debug('runEngine: starting engine_preprocess')  

engPre = engine_preprocess(temp['invoice_path'],temp['invoice_name'])
progressCounter = progressCounter + 3
print(progressCounter)
time.sleep(0.01)

logging.debug('runEngine: engine_preprocess completed')  
logging.debug('runEngine: starting engine_main')  
engMain = engine_main(engPre.invoiceData, temp['destination_path'][0], str(application_path+'/templates/'), str(application_path+'/pdfDummy.pdf'))
logging.debug('runEngine: engine_main completed')  
print(10)
time.sleep(0.01)
dial = wx.MessageDialog(None, "extraction process completed.", 'Info', wx.OK | wx.ICON_INFORMATION)
dial.ShowModal()
