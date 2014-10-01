#!/usr/bin/env python
import sys
import string 

def DictFunction():
    """Print Chris is from Seattle, and he likes chocolate cake, mango fruit,
    greek salad, and lasagna pasta"""
    print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad and {pasta} pasta".format(**food_prefs)
    
def DictFunction2():
    """Build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent"""
    print "Create Second Dictionary"
    NumberDict = dict(zip((i for i in range(16)), (hex(i) for i in range(16))))
    print NumberDict

def DictFunction3():
    """Create new dictionary with count of occurances of the letter 'a' in the values"""
    print "Create Third Dictionary"
    Dictionary3 = {key:value.count("a") for key, value in food_prefs.iteritems()}
    print Dictionary3
    
def SetFunction():
    """create a few sets with numbers divisible by 2, 3, 4 and test if they're subsets of each other"""
    s2 = []
    s3 = []
    s4 = []
    s2 = { i for i in range(21) if i%2 == 0}
    s3 = { i for i in range(21) if i%3 == 0}
    s4 = { i for i in range(21) if i%4 == 0}
    s2 = set(s2)
    s3 = set(s3)
    s4 = set(s4)
    print s3.issubset(s2)
    print s4.issubset(s2)
    


if __name__ == "__main__":
    food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}
    DictFunction()
    DictFunction2()
    DictFunction3()
    SetFunction()
    