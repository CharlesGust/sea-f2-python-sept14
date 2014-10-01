#!/usr/bin/env python

import pathlib
import os

#prints current directory
cwd = os.getcwd()
print "Current Working Directory: " + cwd

#prints all paths to files in current directory
pathd = pathlib.Path('./')
pathd.absolute()

for f in pathd.iterdir():
    print str(pathd.absolute()) + "/" + str(f)