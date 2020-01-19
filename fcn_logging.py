#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 19:07:01 2019

@author: jannik wiessler
"""


def autolog(message,logger):
    "Automatically log the current function details."
    import inspect
    # Get the previous frame in the stack, otherwise it would
    # be this function!!!
    func = inspect.currentframe().f_back.f_code
    # Dump the message + the name of this function to the log.
    logger.debug("message: %s in %s in %s, line: %i" % (
        message, 
        func.co_name,
        func.co_filename, 
        func.co_firstlineno
    ))