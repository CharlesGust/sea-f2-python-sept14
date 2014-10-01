#!/usr/bin/env python
import sys
import string 

def rot13(n):
    """This function will rotate a user defined string 13 characters"""
   # n = str(raw_input('What do you want rotated? :'))
    rot13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
    return string.translate(str(n), rot13)

if __name__ == "__main__":
    assert rot13('z y x') == 'm l k'
    assert rot13('???') == '???'
    assert rot13('A B C') == 'N O P'
    