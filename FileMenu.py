#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:29:12 2019

@author: jannik
"""

import wx
import os

class FileMenu(wx.Menu):
    def __init__(self, parentFrame):
        super().__init__()
        self.OnInit()
        self.parentFrame = parentFrame
    
    def OnInit(self):
        newItem = wx.MenuItem(parentMenu=self, id=wx.ID_NEW, text="&New\tCtrl+N", kind=wx.ITEM_NORMAL)
        self.Append(newItem)

        openItem = wx.MenuItem(parentMenu=self, id=wx.ID_OPEN, text='&Open\tCtrl+O', kind=wx.ITEM_NORMAL)
        self.Append(openItem)
        self.Bind(wx.EVT_MENU, handler=self.onOpen, source=openItem)

        saveItem = wx.MenuItem(parentMenu=self, id=wx.ID_SAVE, text="&Save\tCtrl+S", helpString="Save your file", kind=wx.ITEM_NORMAL)
        self.Append(saveItem)
        self.Bind(wx.EVT_MENU, handler=self.onSave, source=saveItem)

        self.AppendSeparator() 

        radioItem1 = wx.MenuItem(self, id=200, text = "Option 1", kind = wx.ITEM_RADIO)
        self.Append(radioItem1)
        radioItem2 = wx.MenuItem(self, id=300, text = "Option 2", kind = wx.ITEM_RADIO) 
        self.Append(radioItem2)

        self.AppendSeparator() 
        
        quitItem = wx.MenuItem(parentMenu=self, id=wx.ID_EXIT, text='&Quit\tCtrl+Q') 
        self.Append(quitItem)
        self.Bind(wx.EVT_MENU, handler=self.onQuit, source=quitItem)

    def onOpen(self, event):
        wildcard = "TXT files (*.txt)|*.txt"
        dialog = wx.FileDialog(self.parentFrame, "Open Text Files", wildcard=wildcard,
                               style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return None

        path = dialog.GetPath()
        if os.path.exists(path):
            with open(path) as myfile:
                for line in myfile:
                    self.parentFrame.text.WriteText(line)

    def onSave(self, event):
        dialog = wx.FileDialog(self.parentFrame, message="Save your data", 
                            defaultFile="Untitled.txt", style=wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)

        if dialog.ShowModal() == wx.ID_CANCEL:
            return None
        
        path = dialog.GetPath()
        data = self.parentFrame.text.GetValue()
        print(data)
        data = data.split('\n')
        print(data)
        with open(path, "w+") as myfile:
            for line in data:
                myfile.write(line+"\n")


    def onQuit(self, event):
        self.parentFrame.Close()

