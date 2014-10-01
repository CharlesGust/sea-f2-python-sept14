#!/usr/bin/env python
import os

def printfiles():
    """print all files in the current directory"""
    filelist = os.listdir(os.getcwd())
    for i in range(len(filelist)-1):
        print filelist[i] \
    

if __name__ == '__main__':
    printfiles()
