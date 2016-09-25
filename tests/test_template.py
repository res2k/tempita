"""Dicstring."""
import unittest
import platform
import doctest


class TestTempita(unittest.TestCase):
    """Dicstring."""
    def test_template(self):
        if platform.python_implementation == 'CPython':
            doctest.testfile('test_template{}.txt'.format(sys.version))
        else:
            doctest.testfile('test_template.pypytxt')

    def test_template(self):
        doctest.testfile('../docs/index.txt')

if __name__ == "__main__":
    unittest.main()
