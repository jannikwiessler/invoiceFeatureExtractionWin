# date: 2019-12-22
# author: jannik wiessler
# e-mail: jannik.wiessler@googlemail.com
# GUI for invoice feature extraction 

import wx
import os
import sys
import logging
from invoiceFrame import invoiceFrame
from newTemplateFrame import newTemplateFrame

# get current directory: for logger
if getattr(sys, 'frozen', False): 
    application_path = os.path.dirname(sys.executable)
elif __file__:
    application_path = os.path.abspath(__file__)
    application_path = application_path[0:-(len(os.path.basename(__file__))+1)]

class MyApp(wx.App):
    def __init__(self):
        super().__init__()

        self.mainFrame = invoiceFrame(parent=None, title='Invoice Extraction App')
        #self.templateFrame = newTemplateFrame(parent=self.mainFrame,title='New Template')
        self.mainFrame.Show()
        #self.templateFrame.Show()

       
if __name__ == '__main__':
    logging.basicConfig(filename=application_path+'/invoiceExtractGUI.log',
                    level=logging.DEBUG,
                    format='%(asctime)-15s %(name)s %(message)s')
    app = MyApp()
    app.MainLoop()