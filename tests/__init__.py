#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def custom_test_suite():
    if sys.version_info <= (3, 4):
        try:
            import unittest2 as unittest
        except ImportError:
            import unittest
    else:
            import unittest

    return unittest.TestLoader().discover("tests", pattern="*_test.py")
