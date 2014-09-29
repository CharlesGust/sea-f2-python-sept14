#! /usr/bin/python


food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}


# perform subtask #1
def print_Dict():
    display = unicode.format(u"\"{name} is from {city},\
and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta\"",
                             **food_prefs)
    print display


# perform subtasks #2, #3
def print_integer_to_hex():
    # kudos to "Dan Lenski" at http://stackoverflow.com/questions/209840
    keys = range(0, 16)
    values = [hex(x) for x in keys]
    dict1 = dict(zip(keys, values))
    print dict1

    # first try:
    # dict1 = dict.item([k=hex(k) for k in range(0, 16)])
    # kudos to "fortran" at http://stackoverflow.com/questions/1747817
    # Some ambiguity on whether values above 9 should be in form "A" or "0xA"
    dict1 = {k: hex(k) for k in range(0, 16)}
    print dict1


# perform subtask #4
def count_a():
    dict1 = {k: k.count("a") for k in food_prefs}
    print dict1


# perform subtask #5.1
def build_ssets():
    s2 = {v for v in range(0, 21) if v % 2 == 0}
    print s2
    s3 = {v for v in range(0, 21) if v % 3 == 0}
    print s3
    s4 = {v for v in s2 if v % 4 == 0}
    print s4


# perform subtask #5.2
def build_ssetseq():
    s1 = [{v for v in range(0, 21) if v % divisor == 0}
          for divisor in range(2, 5)]
    print s1
