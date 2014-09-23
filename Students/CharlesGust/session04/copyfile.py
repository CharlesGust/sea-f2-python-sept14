#! /usr/bin/python

import sys
""" I'm not sure what error checking to provide, and whether or not
    it is acceptable for the various calls to open() to raise exceptions
    """

def copy_File(src, dst):
    f1 = open(src, "rb")
    if not f1:
        print "ERROR: cannot open source file"
        return
    contents = f1.read()

    """ normally, if dst is a directory, it would be expected the src
        file be copied into that directory. Instead, we're letting
        an exception be raised
        """
    f2 = open(dst, "wb")
    if not f2:
        print "ERROR: cannot open destination file"
        return
    f2.write(contents)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "ERROR: copyfile takes two arguments"
    else:
        copy_File(sys.argv[1], sys.argv[2])
