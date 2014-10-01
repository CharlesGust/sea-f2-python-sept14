#!/usr/bin/env python

import os

cwd= os.getcwdu()
contents= os.listdir(cwd)

for f in contents:
    print os.path.abspath(f)

## "Write a program that copies a file from a source to a destination."
## I believe this has already been accomplished in kata14.py
