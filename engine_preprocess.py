#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:32:27 2019

@author: jannik
"""
from pandas import DataFrame

class engine_preprocess():         
    def __init__(self, invoicepath,invoicename):  
        #consturctor
        self.__invoicename = invoicename # expects list of full names of invoices
        self.__invoicepath = invoicepath # expects list of full pathnames of invoices
        self.dataType =	{
                          'pdf' : 1,
                          'png' : 2,
                          'jpeg': 3,
                          'jpg' : 3} 
        self.invoiceData = self.checkDataTyp()
        
       
    def checkDataTyp(self):
        invoice = self.__invoicename # create local var
        temp1 = len(invoice)*[0] # declare local temp var to create dictonary
        temp2 = len(invoice)*[0]
        for i in range(len(invoice)):       
            currentDataType = invoice[i][invoice[i].find('.')+1:] # get ending of string
#            if currentDataType[-1] == '\n': # cut datatypename from right if it is '\n'
#                temp1[i] = currentDataType[:len(currentDataType)-1]
#            else:
#                temp1[i] = currentDataType[:]
            temp1[i] = currentDataType
            # get currentdataType dont matter if its vaild here
            try: # check vailidty
                temp2[i] = self.dataType[temp1[i]]
            except:
                temp2[i] = -1
        temp = {'name': self.__invoicename,
                'path': self.__invoicepath,
                'typ': temp1,
                'valid': temp2}   
        return DataFrame(temp)        
     