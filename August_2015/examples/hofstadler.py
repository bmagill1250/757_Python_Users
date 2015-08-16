# -*- coding: utf-8 -*-
"""
Generator function for Hfstadler's Q sequence
@author: Brian Magill
@date: 7/12/2015
"""
def q_gen(max_index):

    index = 0 
    Q = list()
    
    while index < max_index:
        
        if index == 0:
        
            n = 1
    
        elif index == 1:
        
            n = 1
        
        else:
        
            n = Q[index - Q[index - 1]] + Q[index -Q[index- 2]]
        
        yield n
    
        Q.append(n)
        index += 1
        
        
        
