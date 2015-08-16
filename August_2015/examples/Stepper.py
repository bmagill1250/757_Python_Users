"""
    Stepper.py
    Brian Magill
    7/13/2015

    Simple example of using class with index access for iteration.
"""

class Stepper(object):

    def __init__(self, max_index):
    
        self.max_index = max_index
        
    def __getitem__(self, index):
    
        if index < 0 or index > self.max_index:
        
            raise IndexError
            
        return index**3 
