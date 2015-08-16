#
#   piping_utils.py
#   2015-07-16
#
#   Source code largely borrowed from David Beazley's talk,
#   "Generator Tricks For Systems Programmers"
#   Presented at PyCon UK 2008
#
#   Python generator equivalents to Unix commands

import os
import fnmatch
import gzip, bz2
import re

def gen_find(filepat,top):

    for path, dirlist, filelist in os.walk(top):
    
        for name in fnmatch.filter(filelist,filepat):
        
             yield os.path.join(path,name)
             
             


def gen_open(filenames):

    for name in filenames:
    
        if name.endswith(".gz"):
        
            yield gzip.open(name)
            
        elif name.endswith(".bz2"):
        
            yield bz2.BZ2File(name)
            
        else:
        
            yield open(name)

            
            
def gen_cat(sources):

    for s in sources:
    
        for item in s:
        
            yield item


def gen_grep(pat, lines):

    patc = re.compile(pat)
    
    for line in lines:
    
        if patc.search(line): 
        
            yield line
