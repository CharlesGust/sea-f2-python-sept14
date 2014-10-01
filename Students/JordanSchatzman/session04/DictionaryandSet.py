#!/usr/bin/env python
import sys
import string 

def dictfunction():
    """Create Simple Dictionary"""
    print Dictionary
    del Dictionary["cake"]
    print Dictionary
    Dictionary[u'fruit'] = 'Mango'
    print Dictionary.keys()
    print Dictionary.values()
    print u"Is cake a key in the dictionary? ",
    print 'cake' in Dictionary
    print u"Is Mango a value in the dictionary?",
    print u"Mango" in Dictionary.values()
    
def dictfunction2():
    """Build a dictionary of numbers from zero to fifteen and the hexadecimal equivalent"""
    print "Create Second Dictionary"
    keys = []
    values = []
    for i in range(16):
        keys.append(i)
        values.append(hex(i))
    zipped = zip(keys, values)
    Dictionary2 = dict(zip(keys, values))
    print Dictionary2

def dictfunction3():
    """Create new dictionary with count of occurances of the letter 'a' in the values"""
    print "Create Third Dictionary"
    Dictionary3 = {}
    for keys in Dictionary:
        Dictionary3[keys] = Dictionary[keys].count('a')
    print Dictionary3
    
def setfunction():
    """create a few sets with numbers divisible by 2, 3, 4 and test if they're subsets of each other"""
    s2 = []
    s3 = []
    s4 = []
    for i in range(21):
        if i%2 == 0:
            s2.append(i)
        if i%3 == 0:
            s3.append(i)
        if i%4 == 0:
            s4.append(i)
    s2 = set(s2)
    s3 = set(s3)
    s4 = set(s4)
    print s3.issubset(s2)
    print s4.issubset(s2)
    
def frozensetfunction():
    """create a frozen set"""
    pythonset = set('Python')
    pythonset.add('i')
    marathonset = frozenset('marathon')
    print pythonset.union(marathonset)
    print pythonset.intersection(marathonset)
    



if __name__ == "__main__":
    Dictionary = {"name": u"Chris",
         u"city": "Seattle",
         u"cake": "chocolate"}
    dictfunction()
    dictfunction2()
    dictfunction3()
    setfunction()
    frozensetfunction()