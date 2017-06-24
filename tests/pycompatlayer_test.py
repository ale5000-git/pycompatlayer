import unittest
import pycompatlayer


class PyCompatLayerTestCase(unittest.TestCase):
    """Tests for `pycompatlayer.py`."""

    def test_fix_all(self):
        self.assertTrue(pycompatlayer.fix_all())

        # The code is executed twice during the test in some cases,
        # this is a workaround to avoid failing.
        # ToDO: Fix the cause
        try:
            import builtins
        except ImportError:
            import __builtin__ as builtins
        del builtins.pycompatlayer

if __name__ == "__main__":
    unittest.main()
