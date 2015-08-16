#!/usr/bin/python
#
#   Using_Loops.py
#   Brian Magill
#   7/16/2015
#

import sys

getLastColumns = lambda file_h: (line.rsplit(None,1)[1] for line in file_h)

filterValidNums = lambda bytestr: (int(bytestr) for bytestr in bytecolumn if bytestr != '-')

argv = sys.argv

if len(argv) != 2:

    print "Usage: %s <log file> " % argv[0]

filename = argv[1]


wwwlog = open(filename)

bytecolumn = getLastColumns(wwwlog)

bytes = filterValidNums(bytecolumn)
        
print "Total", sum(bytes)
