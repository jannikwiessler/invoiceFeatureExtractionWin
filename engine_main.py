#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:29:09 2019

@author: jannik
"""

from pytesseract import image_to_pdf_or_hocr
from fcns import extract_mydata_pdf, get_invoicedata, add_todataframe
from pandas import read_excel
#import pprint
import logging

class engine_main():         
    def __init__(self, invoiceData, destinationPath, templateFolerPath, pdfDummyPath):  
        #consturctor
        self.__writeExcelFlagg = 1 # this is for user interaction in upcomming versions 
        self.__destinationfile = destinationPath
        self.__invoiceData = invoiceData
        # default excel dictionary
        field_dic = {'Lieferdatum' : 'date_service',
                     'Bestelldatum' : 'date_order',
                     'Zulieferer' : 'issuer',
                     'Rechnungsnummer' : 'invoice_number',
                     'Betrag' : 'amount_sum',
                     'Netto' : 'amount_net',
                     'Template' : 'template'}
        
        templatefolder = templateFolerPath
        pdfDummy = pdfDummyPath
        
        for row, info in self.__invoiceData.iterrows():
            if info['valid'] != -1: # we have a vaild datatype
                if info['typ'] != 'pdf': # if ivvoice is not pdf: create pdf
                     logging.debug('egine_main: invoice is not pdf')
                     x = image_to_pdf_or_hocr(info.path,lang='deu')
                     f = open(pdfDummy, "w+b")
                     f.write(bytearray(x))
                     f.close()
                     pdf = pdfDummy   
                else: # invoice is pdf
                     logging.debug('egine_main: invoice is pdf')
                     pdf = info.path

                logging.debug('egine_main: starting extract_mydata_pdf with pdf: '+pdf)    
                text = extract_mydata_pdf(pdf) # get data from created pdf
                logging.debug('egine_main: extract_mydata_pdf completed')
                if text == None:
                    logging.debug('egine_main: extracted text is empty')
                logging.debug('egine_main: starting get_invoicedata')    
                data = get_invoicedata(text,templatefolder,field_dic) #get data from extracted text   
                if data != None:
                    logging.debug('egine_main: data != None')
                else: 
                    logging.debug('egine_main: data == None')
                logging.debug('egine_main: get_invoicedata completed')   
                #pprint.pprint(data)

                # do the xlsx wirting handle
                if self.__writeExcelFlagg == 1 and data != None:
                    logging.debug('egine_main: starting xlsWriting')
                    df = read_excel(self.__destinationfile)
                    logging.debug('egine_main: reading completed')
                    df = add_todataframe(df,field_dic,data)
                    logging.debug('egine_main: adding data completed')
                    df.to_excel(self.__destinationfile,index=False)
                    logging.debug('egine_main: xlsWriting completed')
                
            else: print(info['typ']+' is not supported') 
        