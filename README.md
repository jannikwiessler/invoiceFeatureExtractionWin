# invoiceFeatureExtraction
automatic feature extraction of an invoice

2019-12-23: this will become a mvp and is for now far away from an alpha version. This version is developed and tested on mac os. 

Start GUI via: pythonw Gui_wx.py

User needs to specify features to extract from an issuers type of invoice. (.txt files in templates folder). 
There is already de_MusterGmbH.txt for the invoice rechnungsvorlage-2019.pdf.
One can load one or multiple invoices as well as specify an excel output file (featureOut.xlsx)

Build standalone executable/app (will be too large to upload to github):

The softwares architecture consists of only 2 layers: 1.) Gui, 2.) Engine.

Thus one need to build the package in two steps:

- (1) GUI: pyinstaller Gui_wx.py --onefile --windowed (complete build up takes about <1min)
- (2) Engine: pyinstaller runEngine.py --windowed --onefile (complete build up takes about >5min)

The following data have to be copied in Gui_wx.app->Contents->MacOS
- gs
- magisch
- tesseract
- runEngine
- templates (folder containing the tamplates)

After completing these steps successfully one can use the executable Gui_wx.app without python nor terminal.

Hint: By renaming the app Gui_wx.app dont forget to remane the corresponding executable Gui_wx.app->Contents->MacOS->Gui_wx as well!
