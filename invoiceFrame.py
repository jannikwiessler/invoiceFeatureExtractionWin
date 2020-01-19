#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:28:20 2019

@author: jannik
"""

import wx
from FileMenu import FileMenu
from EditMenu import EditMenu
from TemplateMenu import TemplateMenu
from invoicePanel import invoicePanel        


class invoiceFrame(wx.Frame):         
    def __init__(self, parent, title): 
        super().__init__(parent, title = title, size = (400, 400))  
        self.InitMenus()
        self.InitPannel()
        #self.InitCenterApp()

    def InitMenus(self):   
        #self.text = wx.TextCtrl(parent=self, id=wx.ID_ANY, style = wx.EXPAND|wx.TE_MULTILINE) 
        menuBar = wx.MenuBar() 

        fileMenu = FileMenu(parentFrame=self)
        menuBar.Append(fileMenu, '&File') 

        editMenu = EditMenu()
        menuBar.Append(editMenu, '&Edit')

        templateMenu = TemplateMenu(parentFrame=self)
        menuBar.Append(templateMenu, '&Templates') 

        self.SetMenuBar(menuBar) 

        #self.Bind(wx.EVT_MENU, self.MenuHandler)

    def InitCenterApp(self):
        self.Centre() 
        self.Show(True)
 
    def InitPannel(self):
        self.panel = invoicePanel(parent=self)

