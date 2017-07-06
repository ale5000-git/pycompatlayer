#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys


def custom_test_suite():
    try:
        if sys.version_info <= (3, 4):
            import unittest2 as unittest
        else:
            import unittest
    except ImportError:
        import unittest
    return unittest.TestLoader().discover("tests", pattern="*_test.py")
