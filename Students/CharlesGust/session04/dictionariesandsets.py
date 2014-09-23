#!/usr/bin/python

global_Dictionary = {"name":  "Chris",
                     "city":  "Seattle",
                     "cake":  "Chocolate"}


def perform_SubTask1():
    global global_Dictionary

    print global_Dictionary

    del global_Dictionary["cake"]

    print global_Dictionary

    global_Dictionary["fruit"] = "Mango"

    print global_Dictionary

    for key in global_Dictionary.keys():
        print "Key: %s" % key

    for val in global_Dictionary.values():
        print "Values: ", val

    print global_Dictionary

    print "Cake in Dictionary Keys?: ", "cake" in global_Dictionary.keys()
    print "Mango in Dictionary Values?:", "Mango" in global_Dictionary.values()


def perform_SubTask2():
    keys = range(0, 16)
    vals = []

    """ I don't know how to use zip to create a Dictionary, because it
        creates a list """

    for n in range(0, 16):
        vals.append(str(n) if n < 10 else str(chr(n - 10 + ord('A'))))

    new_Dictionary = zip(keys, vals)

    print new_Dictionary


def perform_SubTask3():

    """ string count method from stackoverflow.com """
    for n in global_Dictionary:
        global_Dictionary[n] = global_Dictionary[n].count('a')

    """ assignment did not say whether to do this in place in the other
        dictionary or create a new one. Because it said "Using the
        dictionary", I thought the dictionary should be used and not
        preserved
        """
    print global_Dictionary


def perform_SubTask4():
    s2 = set()
    s3 = set()
    s4 = set()
    for n in range(0, 20):
        if not n % 2:
            s2.add(n)
        if not n % 3:
            s3.add(n)
        if not n % 4:
            s4.add(n)
    print s2
    print s3
    print s4
    print "Is s3 a subset of s2? ", s3.issubset(s2)
    print "Is s4 a subset of s2? ", s4.issubset(s2)


def perform_SubTask5():
    s1 = set('Python')
    s1.update('i')

    fs1 = frozenset('marathon')

    print s1.union(fs1)
    print s1.intersection(fs1)


if __name__ == "__main__":
    global global_Dictionary

    perform_SubTask1()
    perform_SubTask2()
    perform_SubTask3()
    perform_SubTask4()
    perform_SubTask5()
