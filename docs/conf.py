#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime
import fileinput
import re


def replace_ext_inside_documentation_files(path, filename):
    for line in fileinput.input(path+filename, inplace=1, backup=".bak", mode="rb"):
        # Hack to fix the extension of internal links in the documentation
        sys.stdout.write(re.sub(r"\`(.+)\s<([\w\.]+)\.rst>\`_", r"`\1 <\2.html>`_", line.decode("utf-8")))
    sys.stdout.flush()


def find_and_fix_documentation_files(path):
    dir_list = tuple(sorted(os.listdir(path)))
    if len(dir_list) != 0:
        for filename in dir_list:
            if filename.endswith(".rst"):
                sys.stdout.write("Fixing "+path+filename+" ..." + os.linesep)
                replace_ext_inside_documentation_files(path, filename)
    sys.stdout.write("Done." + os.linesep + os.linesep)
    sys.stdout.flush()


# General information about the project.
project = 'PyCompatLayer'
copyright = '2016-' + str(datetime.datetime.now().year) + ', ale5000'
author = 'ale5000'

find_and_fix_documentation_files("../")
find_and_fix_documentation_files("./")

# The master toctree document.
master_doc = 'index'

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pycompatlayer')))

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.imgconverter'
]
