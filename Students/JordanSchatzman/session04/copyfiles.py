#!/usr/bin/env python
import os
import sys


def copy_file(inputfile, outputfile):
    """copies a file to a destination, from a source"""
    original = open(inputfile, 'rb')
    copy = open(outputfile, 'wb')
    content = original.read()
    output = copy.write(content)



if __name__ == '__main__':
    #The example used here is the mailroom file, it copies it from the my python class folde to desktop.
    copy_file('mailroom.py', 'C:\Users\Jordan\Desktop\mailroom.py')
