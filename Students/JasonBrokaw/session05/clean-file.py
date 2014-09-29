#!/usr/bin/env python

from __future__ import unicode_literals
import sys, io

# def clean_file(*args):
#     """Remove all leading and trailing whitespace from each line of a file"""
#     if not args:
#         print "usage: ./clean-file.py input-filename [output-filename]"
#         print "or clean_file(input-filename[, output-filename])"
#         print "If output-filename is not specified, the input file will be overwritten"
#         return

#     infile = io.open(args[0], 'r')

#     lines = infile.readlines()

#     infile.close()

#     output_filename = args[1] if len(args) > 1 else args[0]
#     outfile = io.open(output_filename, 'w', encoding='utf-8')

#     for line in lines:
#         outfile.write(line.strip() + "\n")
#     outfile.close()

def clean_file_comprehension(*args):
    """Remove all leading and trailing whitespace from each line of a file"""
    if not args:
        print "usage: ./clean-file.py input-filename [output-filename]"
        print "or clean_file_comprehension(input-filename[, output-filename])"
        print "If output-filename is not specified, the input file will be overwritten"
        return
    if len(args) > 1:
        infile = io.open(args[0], 'r', encoding='utf-8')
        outfile = io.open(args[1], 'w', encoding='utf-8')
    else:
        if raw_input("Overwriting file, are you sure (type 'yes'): ") != 'yes':
            print "usage: ./clean-file.py input-filename [output-filename]"
            print "or clean_file_comprehension(input-filename[, output-filename])"
            print "If output-filename is not specified, the input file will be overwritten"
            return
        infile = io.open(args[0], 'r+', encoding='utf-8')
        outfile = infile

    lines = infile.readlines()

    outfile.seek(0)

    outfile.writelines([line.strip() + "\n" for line in lines])
    outfile.close()

if __name__ == '__main__':
    clean_file_comprehension(*sys.argv[1:])
