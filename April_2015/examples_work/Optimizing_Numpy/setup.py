# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 20:59:00 2015

@author: brianmagill
"""

from distutils.core import setup, Extension
from Cython.Build import cythonize

ext = Extension("cython_version", sources=["cython_version.pyx"])

setup(name="pairwise_cython", ext_modules = cythonize([ext]))