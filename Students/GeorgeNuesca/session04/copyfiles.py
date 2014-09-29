#!/usr/bin/env python2.7

import os

def copyfiles():

    cdir = os.listdir(os.getcwd())  # Gets the directory and lists its files.
    for file in cdir:
        print os.path.relpath(file)  # Shows absolute path.

    filein = 0
    while filein not in cdir:
        filein = raw_input('Type a filename from the list to copy or q to quit: ')
        if filein == 'q':
            return

    fileout = raw_input('Type a filename for the new copy: ')
    secverify = 0
    while (fileout in cdir) and (secverify == 0):
        verify = 0
        while verify not in ['y', 'n']:
            verify = raw_input('Do you want to overwrite the file. (y, n) ')
            if verify == 'y':
                secverify = 1
                break
            if verify == 'n':
                fileout = raw_input('Type a different filename for the new copy: ')
                break

    foo = open(filein, 'r')
    text = foo.read()
    foo.close()

    bar = open(fileout, 'w')
    bar.write(text)
    bar.close()

if __name__ == '__main__':
    copyfiles()