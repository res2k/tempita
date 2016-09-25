"""Dicstring."""
import unittest
import platform
import doctest
import sys
import os
from tempita import Template
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


class TestTempita(unittest.TestCase):
    """Dicstring."""
    def test_doctest_template(self):
        if platform.python_implementation == 'CPython':
            doctest.testfile('test_template{}.txt'.format(sys.version))
        else:
            doctest.testfile('test_template.pypytxt')

    def test_doctest_docs_index(self):
        doctest.testfile('../docs/index.txt')

    def test_read_template_from_file_with_encoding(self):
        filename = '/tests/test_basetemplate.txt'
        namespace = dict(name="Arthur Dent")
        t = Template.from_filename(sys.path[0] + filename, namespace=namespace, encoding="latin-1")
        print(t)

    def test_read_template_from_file_without_encoding(self):
        filename = '/tests/test_basetemplate.txt'
        namespace = dict(name="Arthur Dent")
        t = Template.from_filename(sys.path[0] + filename, namespace=namespace, encoding=None)
        print(t)

if __name__ == "__main__":
    unittest.main()
