#!/usr/env/python

def rot13(s):
    return s.encode("rot13")

if __name__ == '__main__':
    #Tests accuracy of rot13 encoding
    assert rot13("This is a test!") == "Guvf vf n grfg!"
    assert rot13("The quick brown fox jumps over the lazy dog.") == \
    "Gur dhvpx oebja sbk whzcf bire gur ynml qbt."
    print "All tests pass."