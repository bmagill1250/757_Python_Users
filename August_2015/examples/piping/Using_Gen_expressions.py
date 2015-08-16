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

bytecolumn = (line.rsplit(None,1)[1] for line in wwwlog) 

bytes = (int(bytestr) for bytestr in bytecolumn if bytestr != '-')
        
print "Total", sum(bytes)
