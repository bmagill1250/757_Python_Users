# -*- coding: utf-8 -*-
"""
Created on Fri Feb 27 15:32:10 2015

@author: brianmagill
"""

cpdef long cp_G(long n):
    """Douglas Hofstadter's G Sequence"""
        
    if n == 0:
        return 0
        
    return n - cp_G(cp_G(n -1))