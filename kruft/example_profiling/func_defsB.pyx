# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 18:58:34 2015

@author: brianmagill
"""

#from math import sin, pi
from math import pi
from libc.math cimport sin

def sinc(double x):
    
    if (x == 0.0):
    
        return 1.0
  
    else:

        return sin(pi*x)/(pi*x)
