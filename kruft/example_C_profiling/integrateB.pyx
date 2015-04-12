# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:16:47 2015

@author: brianmagill
"""

# from math import sin, pi
# 
# def sinc(double x):
#     
# 	if (x == 0.0):
#     
# 		return 1.0
# 		
# 	else:
# 	
# 		return sin(pi*x)/(pi*x)

def trapezoid(f, double a, double b, int n=2000):

    cdef:   
 	
        int i
        double dx = (b - a)/n
        double s = 0.0
    
    for i in range(n):
        
        s += f(a + i*dx)
        
    return s*dx

#
#  Implementation borrowed from Wikipedia
#    
def simpson(f, double a, double b, int n):
    """Approximates the definite integral of f from a to b by the
    composite Simpson's rule, using n subintervals (with n even)"""
 
    cdef:
 	
        int i
        double h
        double s
 		
    if n % 2:
        raise ValueError("n must be even (received n=%d)" % n)
 
    h = (b - a) / n
    s = f(a) + f(b)
 
    for i in range(1, n, 2):
        
        s += 4 * f(a + i * h)
        
    for i in range(2, n-1, 2):
        
        s += 2 * f(a + i * h)
 
    return s * h / 3