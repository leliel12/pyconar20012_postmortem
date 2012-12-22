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

#===============================================================================
# LOGIC
#===============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))

PDF = os.path.join(PATH, "build", "latex", "PyConArgentina2012-PostMortem.pdf")

TO = os.path.join(PATH, "source", "_static")

MAKE = "make.bat {}" if os.name == "nt" else "make {}"


os.system(MAKE.format("clean"))
os.system(MAKE.format("latexpdf"))

shutil.copy(PDF, TO)

os.system(MAKE.format("html"))

