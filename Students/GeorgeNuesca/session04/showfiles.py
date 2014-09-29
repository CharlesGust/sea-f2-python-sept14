#!/usr/bin/env python2.7

import os

def showfiles():
    cdir = os.listdir(os.getcwd())  # Gets the directory and lists its files.

    for file in cdir:
        print os.path.abspath(file)  # Shows absolute path.

if __name__ == '__main__':
    showfiles()