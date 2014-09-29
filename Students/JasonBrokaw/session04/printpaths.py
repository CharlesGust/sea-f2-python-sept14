#!/usr/local/bin/python

import pathlib

if __name__ == '__main__':
    p = pathlib.Path(u'.')
    for filename in p.iterdir():
        print str(filename.absolute())
