# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:58:18 2015
Q_Sequence
@author: brianmagill
@date 7/15/2015
"""

class Q_Sequence:

    def __init__(self, max_index):
        self.Q = list()
        self.i = 0
        self.max_index = max_index

    def __iter__(self):
        return self

    def next(self):
        
        if self.i < self.max_index:
            
            if self.i == 0:
                
                n = 1
                
            elif self.i == 1:
                
                n = 1
            else:
                
                n = self.Q[self.i - self.Q[self.i - 1]] + \
                                self.Q[self.i - self.Q[self.i - 2]]
                
            self.i += 1
            self.Q.append(n)
            
            return n
        else:
            raise StopIteration()
