# invoiceFeatureExtraction
automatic feature extraction of an invoice

2019-12-23: this will become a mvp. This version is developed and tested on win10. 

Start GUI via: python invoiceExtractGUI.py

User needs to specify features to extract from an issuers type of invoice. (.txt files in templates folder). 
There is already de_MusterGmbH.txt for the invoice rechnungsvorlage-2019.pdf.
One can load one or multiple invoices as well as specify an excel output file (featureOut.xlsx)

Build standalone executable/app (will be too large to upload to github):

The softwares architecture consists of only 2 layers: 1.) Gui, 2.) Engine.

Thus one need to build the package in two steps:

- (1) GUI: pyinstaller invoiceExtractGUI.py --onefile --windowed (complete build up takes about <1min)
- (2) Engine: pyinstaller runEngine.py --windowed --onefile (complete build up takes about >5min)

The following data have to be copied in the same folder as invoiceExtractGUI.exe
- gs
- magick
- tesseract
- runEngine
- templates (folder containing the tamplates)

After completing these steps successfully one can use the executable invoiceExtractGUI.app without python nor terminal.
