#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime
import fileinput
import re

# General information about the project.
project = 'PyCompatLayer'
copyright = '2016-' + str(datetime.datetime.now().year) + ', ale5000'
author = 'ale5000'

# Hack to fix the extension of internal links in the generated documentation
for line in fileinput.input("../README.rst", inplace=1, backup=".bak", mode="rb"):
    sys.stdout.write(re.sub(r"\`(.+)\s<([\w\.]+)\.rst>\`_", r"`\1 <\2.html>`_", line.decode("utf-8").rstrip()) + "\n")
sys.stdout.flush()

# The master toctree document.
master_doc = 'index'

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pycompatlayer')))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest'
]
