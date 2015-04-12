# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:59:00 2015

@author: brianmagill
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("mt_random", sources=["mt_random.pyx", "mt19937ar.c"])

setup(name="mersenne_random", ext_modules = cythonize([ext]))