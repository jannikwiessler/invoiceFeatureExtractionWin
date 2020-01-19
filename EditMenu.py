#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:30:22 2019

@author: jannik
"""

import wx


class EditMenu(wx.Menu):
    def __init__(self):
        super().__init__()
        self.OnInit()

    def OnInit(self):
        copyItem = wx.MenuItem(self, 100,text = "Copy",kind = wx.ITEM_NORMAL)
        self.Append(copyItem) 
        cutItem = wx.MenuItem(self, 101,text = "Cut",kind = wx.ITEM_NORMAL) 
        self.Append(cutItem) 
        pasteItem = wx.MenuItem(self, 102,text = "Paste",kind = wx.ITEM_NORMAL) 
        self.Append(pasteItem)
