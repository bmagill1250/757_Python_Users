# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:32:10 2015

@author: brianmagill
"""

def py_G(n):
    
    if n == 0:
        return 0
        
    return n - py_G(py_G(n -1))