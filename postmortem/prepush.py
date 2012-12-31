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

ROOT = os.path.join(PATH, "..", "README.rst")

VERSION_TXT = os.path.join(SOURCE, "version.txt")

ABOUT_RST = os.path.join(SOURCE, "about.rst")

PDF = os.path.join(PATH, "build", "latex", "PyConArgentina2012-PostMortem.pdf")

TO = os.path.join(SOURCE, "_static")

MAKE = "make.bat {}" if os.name == "nt" else "make {}"


#===============================================================================
# LOGIC
#===============================================================================

now = datetime.datetime.now()
ver = now.strftime("%y.%m.%d.%H%M")

print(">>> Frozen version")
with open(VERSION_TXT, "w") as fp:
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

shutil.copy(ABOUT_RST, ROOT)

ex("hg add {}".format(os.path.join(TO, "*.pdf")))
ex("hg add {}".format(ROOT))
ex('hg commit -m "add pdf and readme at {}" -u prepush.py'.format(now))
ex('hg tag {} -u prepush.py'.format(ver))

