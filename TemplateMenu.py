#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:29:12 2019

@author: jannik
"""

import wx
import os
from newTemplateFrame import newTemplateFrame

class TemplateMenu(wx.Menu):
    def __init__(self, parentFrame):
        super().__init__()
        self.OnInit()
        self.parentFrame = parentFrame
    
    def OnInit(self):
        newTemplate = wx.MenuItem(parentMenu=self, id=301, text="&new", kind=wx.ITEM_NORMAL)
        self.Append(newTemplate)
        self.Bind(wx.EVT_MENU, handler=self.onNew, source=newTemplate)

        editTemplate = wx.MenuItem(parentMenu=self, id=302, text='&edit', kind=wx.ITEM_NORMAL)
        self.Append(editTemplate)
        self.Bind(wx.EVT_MENU, handler=self.onEdit, source=editTemplate)

        manageTemplate = wx.MenuItem(parentMenu=self, id=303, text="&manage", helpString="Save your file", kind=wx.ITEM_NORMAL)
        self.Append(manageTemplate)
        self.Bind(wx.EVT_MENU, handler=self.onManage, source=manageTemplate)

        self.AppendSeparator() 

        self.newTemplateFrame = newTemplateFrame(parent=None,title='New Template')

    def onNew(self, event):
        self.newTemplateFrame = newTemplateFrame(parent=None,title='New Template')
        self.newTemplateFrame.Show()
    def onEdit(self, event):
        print(1)
    def onManage(self, event):
        print(2)


  