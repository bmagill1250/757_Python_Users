# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 21:52:54 2015

@author: brianmagill
"""

from vector_string import page, sort_list

lines = page()
print "-----------------"       
print "Original ordering:"
print "-----------------"
for line in lines:
    print line

sorted_lines = sort_list(lines)
print "-----------------"
print "Sorted lines:" 
print "-----------------"
for line in sorted_lines:
    print line
