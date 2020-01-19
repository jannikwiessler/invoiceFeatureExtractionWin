# -*- coding: utf-8 -*-
# this is modified for windows
def to_text(path, language='deu'):
    """Wraps Tesseract 4 OCR with custom language model.

    Parameters
    ----------
    path : str
        path of electronic invoice in JPG or PNG format

    Returns
    -------
    extracted_str : str
        returns extracted text from image in JPG or PNG format

    """
    import subprocess
    #from distutils import spawn
    import tempfile
    import time
    import logging
    import os, sys

    # Check for dependencies. Needs Tesseract and Imagemagick installed.
#    if not spawn.find_executable('tesseract'):
#        raise EnvironmentError('tesseract not installed.')
#    if not spawn.find_executable('magick'):
#        raise EnvironmentError('imagemagick not installed.')
#    if not spawn.find_executable('gs'):
#        raise EnvironmentError('ghostscript not installed.')
       
    
    if getattr(sys, 'frozen', False): 
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.abspath(__file__)
        application_path = application_path[0:-(len(os.path.basename(__file__))+1)]
    
    logging.debug('tesseract4: starting extracting application_path: '+application_path) 
    #with tempfile.NamedTemporaryFile(suffix='.tiff',delete=False) as tf:
        #with open("temp.tiff","rb+") as tf:
        #tempFile=application_path+'/'+'temp.tiff'
        #tf = tempfile.NamedTemporaryFile(suffix='.tiff',delete=False)  # delete = False is windows specific  
    #for i in range(1):
    # Step 1: Convert to TIFF
    tf = application_path+'/tempFile.tiff'
    gs_cmd = [
        application_path+'/gswin64.exe',
        '-q',
        '-dNOPAUSE',
        '-r600x600',
        '-sDEVICE=tiff24nc',
        '-sOutputFile=' + tf,
        path,
        '-c',
        'quit',
    ]
    subprocess.run(gs_cmd)
    #os.system(gs_cmd)
    time.sleep(0)

    # Step 2: Enhance TIFF
    magick_cmd = [
        application_path+'/magick.exe',
        tf,
        '-colorspace',
        'gray',
        '-type',
        'grayscale',
        '-contrast-stretch',
        '0',
        '-sharpen',
        '0x1',
        #'tiff:-',
        tf,
    ]

    logging.debug('tesseract4: starting subprocess p1') 
    subprocess.run(magick_cmd)

    logging.debug('tesseract4: starting subprocess p2') 
    tess_cmd = [application_path+'/Tesseract-OCR/tesseract.exe',
        tf,application_path+'/out',
        '-l', language, 
        '--oem', '1', 
        '--psm', '3', 
        #'stdin', 'stdout'
        ]
    subprocess.run(tess_cmd) # run makes the program wait till subprocess is finished
    time.sleep(0)

    with open(application_path+'/out.txt','rb') as f:
        content = f.read()

    extracted_str = content

    return extracted_str
