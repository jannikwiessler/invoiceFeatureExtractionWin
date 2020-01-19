#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:25:39 2019

@author: jannik
"""

import wx
from newTemplatePanel import newTemplatePanel 

class newTemplateFrame(wx.Frame):
    def __init__(self, parent, title): 
        super().__init__(parent, title = title, size = (360, 570), style = wx.DEFAULT_FRAME_STYLE)    
        self.InitPannel()
        #self.InitCenterApp()
        
    def InitPannel(self):
        self.panel = newTemplatePanel(parent=self)
                 
    def InitCenterApp(self):
        self.Centre() 
        self.Show(True)

    def onDestroy(self):
        self.Destroy()