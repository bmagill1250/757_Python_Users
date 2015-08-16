#!/usr/bin/python
#
#   Using_Loops.py
#   Brian Magill
#   7/16/2015
#

import sys

argv = sys.argv

if len(argv) != 2:

    print "Usage: %s <log file> " % argv[0]
    sys.exit()

filename = argv[1]

wwwlog = open(filename)

total = 0   

for line in wwwlog:

    bytestr = line.rsplit(None,1)[1]
    
    if bytestr != '-':
    
        total += int(bytestr)
        
print "Total", total
