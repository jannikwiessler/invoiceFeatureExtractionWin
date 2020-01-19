#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:23:20 2019

@author: jannik
"""

# tbd:
# 2020-01-04: progress dlg bar


import wx
import time
from newTemplateFrame import newTemplateFrame
import os
import sys
import logging
import subprocess
from shutil import copyfile

class invoicePanel(wx.Panel):
    # A panel is a window on which controls are placed. (e.g. buttons and text boxes)
    # wx.Panel class is usually put inside a wxFrame object. This class is also inherited from wxWindow class.
    def __init__(self,parent):
        super().__init__(parent=parent)
        # create panel properies
        self.__destinationfile_path = []
        self.__pathnames = []
        self.__filenames = []
        self.__percent = 0
        self.__maximum = 100
        
        # add a hello message to the panel
        #welcomeText = wx.StaticText(self, label="To learn wxPython, click the link below!", pos=(20,20))

        # add the load invoice button 
        self.__button_load_invoice = wx.Button(parent=self, label='load invoice', pos = (30, 40))
        self.__button_load_invoice.Bind(wx.EVT_BUTTON, self.__load_invoice_button_onSubmit) # bind action to button
        
        # add the delete invoice button to delete single or multiple data from list box
        self.__button_delete_invoice = wx.Button(parent=self, label='delete', pos = (30, 180))
        self.__button_delete_invoice.Bind(wx.EVT_BUTTON, self.__delete_invoice_button_onSubmit) # bind action to button

        # add the delete invoice button to clear all data from list box
        self.__button_clear_invoice = wx.Button(parent=self, label='clear all', pos = (130, 180))
        self.__button_clear_invoice.Bind(wx.EVT_BUTTON, self.__clear_invoice_button_onSubmit) # bind action 

        # add the check invoice button to search for templates
        self.__button_check_invoice = wx.Button(parent=self, label='extract', pos = (230, 180))
        self.__button_check_invoice.Bind(wx.EVT_BUTTON, self.__check_invoice_button_onSubmit) # bind action 

        # disable control buttons
        self.__enable_disable_control_buttons(0)

        # add list box
        self.__listBox = wx.ListBox(parent=self, pos=(30, 70), size=(280, 100),
        choices=[], style=wx.LB_MULTIPLE, validator=wx.DefaultValidator, name="ListBoxNameStr")

        # add destination file (xlsx)
        self.__button_destination_file = wx.Button(parent=self, label='load file', pos = (240,268))
        self.__button_destination_file.Bind(wx.EVT_BUTTON, self.__load_destination_button_onSubmit) # bind action to button
        
        self.__destination_file = wx.ComboBox(self, wx.CB_SIMPLE, pos=(30,270), size = (200,30), choices=[])

        # add open template window button % tbd asap
        #self.__button_new_template_frame = wx.Button(parent=self, label='template', pos = (400,275))
        #self.__button_new_template_frame.Bind(wx.EVT_BUTTON, self.__add_new_template_frame) # bind action to button
        

        # add test button for progress bar
#        self.__test_button = wx.Button(parent=self, label='progess bar', pos = (30,320))
#        self.__test_button.Bind(wx.EVT_BUTTON, self.__show_processdialog) # bind action to button
        
        self.__font_staticBoxes = wx.Font(18, wx.ROMAN, wx.ITALIC, wx.NORMAL)
        self.__invoicedata_staticBox = wx.StaticBox(self, wx.ID_ANY, "Invoice Data", pos=(10,10),size=(350,220))
        self.__destinationfile_staticBox = wx.StaticBox(self, wx.ID_ANY, "Desitnation File",pos=(10,240),size=(350,80))
        

    def __load_invoice_button_onSubmit(self, event):
        # stuff for the submit button to do
        with wx.FileDialog(self, "Open xc file", wildcard="load invoice (*pdf,*.jpeg,*jpg,*.png)|*pdf;*.jpeg;*jpg;*.png",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            
            self.__pathnames.extend(fileDialog.GetPaths())
            self.__filenames.extend(fileDialog.GetFilenames())
            
            print(self.__pathnames)
            print(self.__filenames)
            print(fileDialog.GetFilenames())
            
            self.__listBox.InsertItems(fileDialog.GetFilenames(), self.__listBox.Count)
            
            if self.__listBox.Count > 0: # endable control buttons 
                self.__enable_disable_control_buttons(1)
                
    def __delete_invoice_button_onSubmit(self, event):
        temp = self.__listBox.GetSelections()     
        for i in reversed(temp): # delete the selections going beackwards!
            self.__listBox.Delete(i)
            del self.__pathnames[i] 
            del self.__filenames[i]
            print(self.__filenames)
            print(self.__pathnames)
        
    def __clear_invoice_button_onSubmit(self, event): 
        dial = wx.MessageDialog(None, 'Clear whole invoice-list ?', 'Warning', 
        wx.YES_NO | wx.ICON_INFORMATION)
        if dial.ShowModal() == wx.ID_YES:
            self.__pathnames = []
            self.__filenames = []
            for i in range(self.__listBox.Count):
                self.__listBox.Delete(0)
            self.__enable_disable_control_buttons(0)    
            
    def __check_invoice_button_onSubmit(self, event):  
        # get current directory: specs must be in same folder ! user has to ensure to have executalbes in same folder
        if getattr(sys, 'frozen', False): 
            temp = os.path.dirname(sys.executable)
        elif __file__:
            temp = os.path.abspath(__file__)
            temp = temp[0:-(len(os.path.basename(__file__))+1)]
        self.__application_path = temp

        if len(self.__destinationfile_path) == 0: # if user did not define destination file 
            logging.debug('invoicePanel: user did not spec destination file (*.xlsx)')
            desktop = os.path.expanduser("~/Desktop") # get path of desktop (should work on all os)
            copyfile(temp+'/Header.xlsx', desktop+'/out.xlsx')
            self.__destinationfile_path.append(desktop+'/out.xlsx')
            
        logging.debug('__check_invoice_button_onSubmit: applicationPath: '+self.__application_path)
        print(self.__application_path)    
        print(self.__destinationfile_path[0]) # need rework asap this is ugly hard code !    
        print(self.__filenames)
        print(self.__pathnames)
        logging.debug('__check_invoice_button_onSubmit: starting __provideDataforEngine')
        self.__provideDataforEngine(self.__pathnames, self.__filenames, self.__destinationfile_path,self.__application_path)
        logging.debug('__check_invoice_button_onSubmit: __provideDataforEngine completed')
        logging.debug('__check_invoice_button_onSubmit: starting __startEngine')
        self.__startEngine(self.__application_path) 
        logging.debug('__check_invoice_button_onSubmit: __startEngine completed')
   
    def __provideDataforEngine(self,invoicePath, invoiceName, destinationPath, exePath):            
        with open(exePath+'/invoice_Path.txt', 'w') as f:
            f.write('invoice_path:\n')
            for item in invoicePath:
                f.write("%s\n" % item)
            f.write('invoice_name:\n')
            for item in invoiceName:
                f.write("%s\n" % item)
            f.write('destination_path:\n')
            for item in destinationPath:
                f.write("%s\n" % item)
            
    def __startEngine(self, exePath):
        self.__show_processdialog()
        logging.debug('__startEngine: subprocess starting')
        p = subprocess.Popen(exePath+'/runEngine',
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.DEVNULL,
            bufsize=64)
        logging.debug('__startEngine: subprocess running') 
        x=0
        while p.poll() is None:
        #   x = p.stdout.readline().decode() #decode bytes but don't strip linefeeds
            x = x+0.00005
            if x < 100:
                self.__update_processdialog(percent=x)
            #wx.GetApp().Yield() # Yield to MainLoop for interactive Gui
        self.__destoryProgress()

    

    def __load_destination_button_onSubmit(self,event):
        with wx.FileDialog(self, "Open xlsx file", wildcard="pdf files (*.xlsx)|*.xlsx",
                       style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST | wx.FD_MULTIPLE) as fileDialog:

            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return     # the user changed their mind
            
            self.__destinationfile_path = fileDialog.GetPaths()
            self.__destinationfile_name = fileDialog.GetFilenames()
            
            self.__destination_file.SetValue(self.__destinationfile_name[0])
            self.__destination_file.Insert(self.__destinationfile_name,0)
            
            print(self.__destinationfile_path)
            print(self.__destinationfile_name)
        
    def __enable_disable_control_buttons(self,n):
        if n == 0:
            self.__button_delete_invoice.Disable()
            self.__button_clear_invoice.Disable()
            self.__button_check_invoice.Disable()
        elif n == 1:
            self.__button_delete_invoice.Enable()
            self.__button_clear_invoice.Enable()
            self.__button_check_invoice.Enable()
            
    def __show_processdialog(self):
        print('progress')
        self.__progress = wx.ProgressDialog('extract innvoice', 'please wait',
                                          maximum=self.__maximum, parent=self,
                                          style=wx.PD_SMOOTH|
                                          wx.PD_AUTO_HIDE|
                                          wx.PD_APP_MODAL)
        #self.__destoryProgress()
        
    def __update_processdialog(self,percent):
        (keepGoing, skip) = self.__progress.Update(percent)

            
    def __destoryProgress(self):
        print('end progressdlg')
        self.__progress.Destroy()
        self.__percent = 0
        
    def __add_new_template_frame(self,event):    
        frame = newTemplateFrame(parent=None, title='Create new invoice-template')
        frame.Show()
        