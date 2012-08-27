#!/usr/bin/env python
"""
 python-term-search
 No copyright

 This program was constructed by members of the python community.

 Candace Cheney, David Mertz, Steve Holden, Peter Banka and Kevin Turner
"""
import sys
#So that we don't have to use a prefix throughout the program.
from glob import iglob
from os.path import isfile
if len(sys.argv) < 3:
    print "USAGE: search <path> <search_term>"
#TODO Figure out a way to flip the order of arguments so that it will be easier to search through multiple files. Then, you can use * in the shell and bash will expand that for you and python will get a list of multiple files to search through.
    sys.exit()
path, search_term = sys.argv[1:]
names = iglob(path)
for name in names:
    if not isfile(name):
        continue
    fh = open(name)
    text = fh.read()
    if search_term in text:
        print "found in", name

