#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:01:11 2019

@author: jannik
"""
import wx
import sys, os
class newTemplatePanel(wx.Panel):
    def __init__(self,parent):
        super().__init__(parent=parent)        
        
        xPosText = 40
        xLenText = 100
        yLenText = 20

        xPosBoxes = 150
        xLenBoxes = 150
        yLenBoxes = yLenText+2

        ySpaceBox = 30

        self.__tb1 = wx.StaticBox(self, wx.ID_ANY, "Info Template", pos=(20,10),size=(300,100))
        self.__tb1.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.__tb2 = wx.StaticBox(self, wx.ID_ANY, "Keywords",pos=(20,120),size=(300,130))
        self.__tb2.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))
        self.__tb3 = wx.StaticBox(self, wx.ID_ANY, "Features",pos=(20,270),size=(300,200))
        self.__tb3.SetFont(wx.Font(9, wx.SWISS, wx.NORMAL, wx.BOLD))

        # infos
        self.__ST1 = wx.StaticText(self, id=wx.ID_ANY, label="Template Name:", pos=(xPosText,42),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC1 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes,40), size=(xLenBoxes,yLenBoxes), style=0)
        self.__ST1b = wx.StaticText(self, id=wx.ID_ANY, label="Zulieferer:", pos=(xPosText,42+ySpaceBox),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC1b = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes,40+ySpaceBox), size=(xLenBoxes,yLenBoxes), style=0)

        # keywords
        self.__ST2 = wx.StaticText(self, id=wx.ID_ANY, label="Keyword 1:", pos=(xPosText,152),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC2 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes,150), size=(xLenBoxes,yLenBoxes), style=0)
        self.__ST3 = wx.StaticText(self, id=wx.ID_ANY, label="Keyword 2", pos=(xPosText,152+ySpaceBox),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC3 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes,150+ySpaceBox), size=(xLenBoxes,yLenBoxes), style=0)
        self.__ST4 = wx.StaticText(self, id=wx.ID_ANY, label="Keyword 3", pos=(xPosText,152+2*ySpaceBox),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC4 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes,150+2*ySpaceBox), size=(xLenBoxes,yLenBoxes), style=0)

        xLenText = 80
        xPosBoxes1 = 130
        xLenBoxes1 = 80
        xPosBoxes2 = xPosBoxes1 + xLenBoxes1 + 10
        xLenBoxes2 = 80
        counter = 0

        # features
        choiceBrutto1 = sorted(['Gesamt','Brutto','Summe','Gesamtbetrag'])
        self.__ST5 = wx.StaticText(self, id=wx.ID_ANY, label="Brutto:", pos=(xPosText,302+ySpaceBox*counter),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC5 = wx.ComboBox(self, id=wx.ID_ANY, value=choiceBrutto1[0], pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes1,yLenBoxes), style=wx.CB_DROPDOWN|wx.CB_SORT,choices=choiceBrutto1)
        self.__TC6 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        counter = counter + 1
        self.__ST6 = wx.StaticText(self, id=wx.ID_ANY, label="Netto:", pos=(xPosText,302+ySpaceBox*counter),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC7 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes1,yLenBoxes), style=0)
        self.__TC8 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        counter = counter + 1
        self.__ST7 = wx.StaticText(self, id=wx.ID_ANY, label="Bestelldatum:", pos=(xPosText,302+ySpaceBox*counter),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC9 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes1,yLenBoxes), style=0)
        self.__TC10 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        counter = counter + 1
        self.__ST8 = wx.StaticText(self, id=wx.ID_ANY, label="Lieferdatum:", pos=(xPosText,302+ySpaceBox*counter),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC11 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes1,yLenBoxes), style=0)
        self.__TC12 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        counter = counter + 1
        self.__ST9 = wx.StaticText(self, id=wx.ID_ANY, label="Rechnungsnr.:", pos=(xPosText,302+ySpaceBox*counter),size=(xLenText,yLenText), style=wx.ALIGN_CENTER_VERTICAL)
        self.__TC13 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes1,yLenBoxes), style=0)
        self.__TC14 = wx.TextCtrl(self, id=wx.ID_ANY, value='', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        counter = counter + 2
        self.__saveButton = wx.Button(self, label='save', pos=(xPosBoxes1,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes))
        self.__saveButton.Bind(wx.EVT_BUTTON, self.__saveButton_onSubmit)
        self.__cancelButton = wx.Button(self, id=wx.ID_ANY, label='cancel', pos=(xPosBoxes2,300+ySpaceBox*counter), size=(xLenBoxes2,yLenBoxes), style=0)
        self.__cancelButton.Bind(wx.EVT_BUTTON, self.__cancelButton_onSubmit)

    def __saveButton_onSubmit(self,event):
        if getattr(sys, 'frozen', False): 
            application_path = os.path.dirname(sys.executable)
        elif __file__:
            application_path = os.path.abspath(__file__)
            application_path = application_path[0:-(len(os.path.basename(__file__))+1)]
        if not self._newTemplatePanel__TC1.Value:
            dial = wx.MessageDialog(None, 'Template Name is missing.', 'Warning', wx.OK | wx.ICON_INFORMATION)
            dial.ShowModal()
        else:
            with open(application_path+'/templates/'+self._newTemplatePanel__TC1.Value+'.txt','w') as f:
                f.write("issuer:\n- '"+self._newTemplatePanel__TC1b.Value+"'\n")
                f.write("fields:\n")
                f.write("- amount_sum: '"+self._newTemplatePanel__TC5.Value+"\s*"+self._newTemplatePanel__TC6.Value+"'\n")
                f.write("- amount_net: '"+self._newTemplatePanel__TC7.Value+"\s*"+self._newTemplatePanel__TC8.Value+"'\n")
                f.write("- date_order: '"+self._newTemplatePanel__TC9.Value+"\s*"+self._newTemplatePanel__TC10.Value+"'\n")
                f.write("- date_service: '"+self._newTemplatePanel__TC11.Value+"\s*"+self._newTemplatePanel__TC12.Value+"'\n")
                f.write("- invoice_number: '"+self._newTemplatePanel__TC13.Value+"\s*"+self._newTemplatePanel__TC14.Value+"'\n")
                f.write("keywords:\n")
                f.write("- '"+self._newTemplatePanel__TC2.Value+"'\n")
                f.write("- '"+self._newTemplatePanel__TC3.Value+"'\n")
                f.write("- '"+self._newTemplatePanel__TC4.Value+"'\n")
            dial = wx.MessageDialog(None, "'"+self._newTemplatePanel__TC1.Value+"'"+"created successfully.", 'Info', wx.OK | wx.ICON_INFORMATION)
            dial.ShowModal()
            self.Parent.Destroy()
    
    def __cancelButton_onSubmit(self,event):
        self.Parent.Destroy()
