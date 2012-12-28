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

SOURCE = os.path.join(PATH, "source")

VERSION_TXT = os.path.join(SOURCE, "version.txt")

PDF = os.path.join(PATH, "build", "latex", "PyConArgentina2012-PostMortem.pdf")

TO = os.path.join(SOURCE, "_static")

MAKE = "make.bat {}" if os.name == "nt" else "make {}"

#===============================================================================
# LOGIC
#===============================================================================
import sys; sys.exit(0)
print("frozen version")
with open(VERSION_TXT, "w") as fp:
    ver = datetime.datetime.now().strftime("%y.%m.%d.%M%S")
    fp.write(ver)

def ex(cmd):
    print(">> Start '{}'...".format(cmd))
    os.system(cmd)
    print(">> Finish '{}'".format(cmd))

os.chdir(PATH)

ex(MAKE.format("clean"))
ex(MAKE.format("latexpdf"))

shutil.copy(PDF, TO)
print(">> Copied '{}' -> '{}'".format(PDF, TO))

ex("hg add {}".format(TO))
ex('hg commit -m "add pdf at {}" -u prepush.py'.format(datetime.datetime.now()))


