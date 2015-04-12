# -*- coding: utf-8 -*-
from math import fabs

import pyximport
pyximport.install()

#from integrate import trapezoid, simpson
from integrateB import trapezoid, simpson
#from func_defs import sinc
from func_defsB import sinc
#from integrateB import trapezoid, simpson, sinc

   
def main():
    
    a, b = -10000.0, 0.0
    
    actual_value = 0.5
    
#    x = trapezoid(sinc, a, b, n=5000000)
    x = simpson(sinc, a, b, n=50000)
    print "sinc integral = ", x
    print "rel error = ", fabs(x - actual_value)/actual_value
    
if __name__ == '__main__':
    
    import cProfile
    
    cProfile.run('main()', sort='time')
