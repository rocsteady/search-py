#!/usr/bin/env python
import sys
from glob import iglob
from os.path import isfile
if len(sys.argv) < 3:
   print "USAGE: search <path> <search_term>"
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