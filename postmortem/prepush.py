#!/usr/bin/env python
# -*- coding: utf-8 -*-

#===============================================================================
# DOC
#===============================================================================

"""This module build pdf and put inside static directory of html"""


#===============================================================================
# IMPORT
#===============================================================================

import os
import shutil
import datetime

#===============================================================================
# CONSTANTS
#===============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))

PDF = os.path.join(PATH, "build", "latex", "PyConArgentina2012-PostMortem.pdf")

TO = os.path.join(PATH, "source", "_static")

MAKE = "make.bat {}" if os.name == "nt" else "make {}"

#===============================================================================
# LOGIC
#===============================================================================

def ex(cmd):
    print(">> Start '{}'...".format(cmd))
    os.system(cmd)
    print(">> Finish '{}'".format(cmd))

os.chdir(PATH)

ex(MAKE.format("clean"))
ex(MAKE.format("latexpdf"))

shutil.copy(PDF, TO)
print(">> Copied '{}' -> '{}'".format(PDF, TO))

ex('hg commit -m "add pdf at {}" -u prepush.py'.format(datetime.datetime.now()))


