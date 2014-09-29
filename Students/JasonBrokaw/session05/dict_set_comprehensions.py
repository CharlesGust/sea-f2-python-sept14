#!/usr/bin/env python

from __future__ import unicode_literals

food_prefs = {"name": u"Chris",
              u"city": u"Seattle",
              u"cake": u"chocolate",
              u"fruit": u"mango",
              u"salad": u"greek",
              u"pasta": u"lasagna"}

#STEP 1
print "STEP 1"

likes_format_list = ["{{{key}}} {key}".format(key=key) for key in food_prefs\
                                        if key != "name" and key != "city"]

likes_format_list[-1] = "and " + likes_format_list[-1] + "."

format_string = "{name} is from {city} and he or she likes " + ", ".join(likes_format_list)

print format_string.format(**food_prefs)

#STEP 2
print "STEP 2"
hex_dict = dict(enumerate([hex(i) for i in range(16)]))
print hex_dict

#STEP 3
print "STEP 3"
hex_dict = {i: hex(i) for i in range(16)}

print hex_dict

#STEP 4
print "STEP 4"
a_counts = {key: food_prefs[key].count('a') for key in food_prefs}
print a_counts

#STEP 5
print "STEP 5"
#5a
s2 = {i for i in range(21) if not i % 2}
s3 = {i for i in range(21) if not i % 3}
s4 = {i for i in range(21) if not i % 4}
print "5a, built line-by-line"
print s2, s3, s4
#5b
multiples = []
for n in range(2,5):
    multiples.append({i for i in range(21) if not i % n})
print "5b, built in a loop"
print multiples[0], multiples[1], multiples[2]
print multiples
#5c
print "5c, built in nested comprehension"
multiples = [{i for i in range(21) if not i % n} for n in range(2,5)]
print multiples[0], multiples[1], multiples[2]
print multiples


