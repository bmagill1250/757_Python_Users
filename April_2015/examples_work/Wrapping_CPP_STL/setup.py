# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:59:00 2015

@author: brianmagill
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("vector_string", sources=["vector_string.pyx"],
                language="c++")

setup(name="vector_string", ext_modules = cythonize([ext]))