#! /usr/bin/python
# coding: latin-1

# -o option to overwrite existing file
import sys
import string


"""
    CMGTODO: argument_error should probably raise an exception, or the caller
     has to remember to return afterwards
"""


def argument_error():
    print "%s: wrong number of arguments; use (-o src) or (src dst)" %\
        sys.argv[0]


def remove_whitespace(contents):
    whitechars = string.whitespace
    return contents


def copy_file():
    src_filename = sys.argv[2] if sys.argv[1] == '-o' else sys.argv[1]
    dst_filename = sys.argv[2]

    src_f = open(src_filename, "r")
    if not src_f:
        print "ERROR: cannot open source file"
        return
    contents = src_f.read()
    src_f.close()

    dst_f = open(dst_filename, "w")
    if not dst_f:
        print "ERROR: cannot open destination file"
        return

    contents = remove_whitespace(contents)
    dst_f.write(contents)
    return

if __name__ == "__main__":
    if len(sys.argv) != 3:
        argument_error()
    else:
        copy_file()
