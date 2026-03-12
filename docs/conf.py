#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: NONE
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder
# For the full list of built-in configuration values, see the documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

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


# Project information
project = 'PyCompatLayer'
author = 'ale5000'
copyright = '2016-' + str(datetime.datetime.now().year) + ', ale5000'

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
    'sphinx.ext.imgconverter',
    'sphinx_rtd_theme'
]

# Options for HTML output
html_theme = 'sphinx_rtd_theme'
html_context = {
    'display_github': True,
    'github_user': 'ale5000-git',
    'github_repo': 'pycompatlayer',
    'github_version': 'master',
    'conf_py_path': '/docs/'
}
