# -*- coding: utf-8 -*-
# 2019-31-12: this is modified for windows
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
#    from distutils import spawn
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
    with tempfile.NamedTemporaryFile(suffix='.tiff',delete=False) as tf:
        # Step 1: Convert to TIFF
        gs_cmd = [
            application_path+'/gswin64.exe',
            '-q',
            '-dNOPAUSE',
            '-r600x600',
            '-sDEVICE=tiff24nc',
            '-sOutputFile=' + tf.name,
            path,
            '-c',
            'quit',
        ]
        subprocess.run(gs_cmd)
        time.sleep(0)

        # Step 2: Enhance TIFF
        magick_cmd = [
            application_path+'/magick.exe',
            tf.name,
            '-colorspace',
            'gray',
            '-type',
            'grayscale',
            '-contrast-stretch',
            '0',
            '-sharpen',
            '0x1',
            'tiff:-',
        ]
        logging.debug('tesseract4: starting subprocess p1') 
        p1 = subprocess.Popen(magick_cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
         
        tess_cmd = [application_path+'/Tesseract-OCR'+'/tesseract.exe',
         '-l', language, 
         '--oem', '1', 
         '--psm', '3', 
         'stdin', 'stdout'
         ]
        logging.debug('tesseract4: starting subprocess p2')
        p2 = subprocess.Popen(tess_cmd, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        logging.debug('tesseract4: starting communication p2')
        out, err = p2.communicate()

        extracted_str = out

        return extracted_str
