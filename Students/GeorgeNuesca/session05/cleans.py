#!/usr/bin/env python2.7

import string
import os

def cleans():

    cdir = os.listdir(os.getcwd())  # Gets the directory and lists its files.
    print cdir

    filename = 1
    while filename not in cdir:
        filename = raw_input('Choose a valid file: ')

    foo = open(filename, 'r')
    reading = foo.readlines()
    foo.close()

    newer = []
    [newer.append(string.strip(read)) for read in reading]
    # newer = map(string.strip, reading)

    newerer = ''.join([new + '\n' for i, new in enumerate(newer)])
    # for i, new in enumerate(newer):
    #     newer[i] = new + '\n'
    # newerer = ''.join(newer)

    writeover = 0
    while writeover not in ['y','n']:
        writeover = raw_input('Would you like to overwrite the file? (y,n): ')
        if writeover == 'y':
            foo = open(filename, 'w')
            foo.write(newerer)
            foo.close()
            break
        elif writeover == 'n':
            newfile = raw_input('Specify new file: ')
            bar = open(newfile, 'w')
            bar.write(newerer)
            bar.close()
            break

if __name__ == '__main__':
    cleans()