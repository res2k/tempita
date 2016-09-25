#!/usr/bin/env python
from setuptools import find_packages
import sys
import os

# Ridiculous as it may seem, we need to import multiprocessing and logging here
# in order to get tests to pass smoothly on python 2.7.
try:
    import multiprocessing
    import logging
    assert multiprocessing
    assert logging
except:
    pass


version = '0.5.1'


kwargs = {}
try:
    from setuptools import setup
    assert setup
except ImportError:
    from distutils.core import setup


setup(name='Tempita',
      version=version,
      description="A very small text templating language",
      long_description="""\
Tempita is a small templating language for text substitution.

This isn't meant to be the Next Big Thing in templating; it's just a
handy little templating language for when your project outgrows
``string.Template`` or ``%`` substitution.  It's small, it embeds
Python in strings, and it doesn't do much else.

You can read about the `language
<http://pythonpaste.org/tempita/#the-language>`_, the `interface
<http://pythonpaste.org/tempita/#the-interface>`_, and there's nothing
more to learn about it.
""",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Topic :: Text Processing',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
      ],
      keywords='templating template language html',
      author='Ian Bicking',
      author_email='ianb@colorstudy.com',
      url='http://pythonpaste.org/tempita/',
      license='MIT',
      packages=['tempita'],
      install_requires=['six'],
      tests_require=['nose'],
      test_suite='nose.collector',
      include_package_data=True,
      zip_safe=True,
      **kwargs
      )
