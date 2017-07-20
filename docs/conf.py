#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc'
]

sys.path.insert(0, os.path.realpath(os.path.join(os.path.dirname(__file__), '..', 'pycompatlayer')))
