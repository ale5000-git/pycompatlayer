#!/usr/bin/env python
# -*- coding: utf-8 -*-
# SPDX-FileCopyrightText: NONE
# SPDX-License-Identifier: CC0-1.0

# Configuration file for the Sphinx documentation builder
# For the full list of built-in configuration values, see the documentation: https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import subprocess
import sys

from docutils import nodes
from sphinx import addnodes
from sphinx.util import logging


def get_revision():
    # Try Read the Docs env vars first
    git_rev = os.environ.get('READTHEDOCS_GIT_COMMIT_HASH')
    git_id = os.environ.get('READTHEDOCS_GIT_IDENTIFIER')
    if git_rev:
        git_rev = git_rev[:8]
        return f"{git_rev} ({git_id})" if git_id else git_rev

    # Local Git fallback
    try:
        return subprocess.check_output(
            ['git', 'rev-parse', '--short=8', 'HEAD'], stderr=subprocess.DEVNULL
        ).decode('utf-8').strip()
    except Exception:
        return None


def transform_rst_links(app, doctree):
    """
    Automatically converts internal .rst file links to Sphinx cross-references
    (:doc: or :ref:), enabling validation and proper path resolution.
    """
    # Traverse only reference nodes that have a 'refuri' attribute
    for node in doctree.findall(nodes.reference):
        uri = node.get('refuri', '')
        if '.rst' not in uri or uri.startswith(('http', 'mailto:', '//')):
            continue

        parts = uri.split('#', 1)
        has_anchor = len(parts) > 1
        reftype = 'ref' if has_anchor else 'doc'
        reftarget = parts[1] if has_anchor else parts[0].removesuffix('.rst')
        logger.info(f"[DEBUG] Converting {uri} -> :{reftype}:`{reftarget}`")

        # Create pending_xref node which Sphinx resolves during build phase
        new_node = addnodes.pending_xref(
            '',
            reftype=reftype,
            refdomain='std',
            reftarget=reftarget,
            refwarn=True,
            refexplicit=True
        )
        # Transfer children (the link text) and replace the original node
        new_node.extend(node.children)
        node.replace_self(new_node)


def setup(app):
    # Hook to modify the document structure before rendering
    app.connect('doctree-read', transform_rst_links)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True
    }


logger = logging.getLogger(__name__)

# Project information
project = 'PyCompatLayer'
author = 'ale5000'
copyright = '2016-%Y ale5000'

revision = get_revision()
if revision:
    copyright += f" | Revision: {revision}"

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
