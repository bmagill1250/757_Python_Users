# -*- coding: utf-8 -*-
from math import pi, sin

import pyximport
pyximport.install()

from integrate import trapezoid, simpson
#from integrateB import trapezoid, simpson
#from math import exp, pi, sqrt, fabs
from math import sin, pi, fabs
#import integrateB

# def expn2(x):
#     
#     return exp(-(x*x/2.))

def sinc(x):
    
    if (x == 0.0):
    
    	return 1.0
    else:
    
    	return sin(pi*x)/(pi*x)


   
def main():
    
    a, b = -10000.0, 0.0
    
    actual_value = 0.5
    
    x = trapezoid(sinc, a, b, n=1000000)
    print "sinc integral = ", x
    print "rel error = ", fabs(x - actual_value)/actual_value
    
if __name__ == '__main__':
    
    import cProfile
    
    cProfile.run('main()', sort='time')
