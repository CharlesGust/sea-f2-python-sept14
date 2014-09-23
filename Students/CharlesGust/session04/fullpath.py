#! /usr/bin/python

import os


def print_Directory1():
    """ using listdir, display full path of files in current directory """
    for fname in os.listdir("./"):
        print os.path.abspath(fname)


if __name__ == "__main__":
    print_Directory1()
