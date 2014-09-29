#!/usr/local/bin/python

import sys, io

def copyfile(source_name, destination_name):
    """Copies contents of source to destination (overwrites destination!)"""
    sourcefile = io.open(source_name, 'r')
    destfile = io.open(destination_name, 'w')
    destfile.write(sourcefile.read())

if __name__ == '__main__':
    copyfile(sys.argv[1], sys.argv[2])
