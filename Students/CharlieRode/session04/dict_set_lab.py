#!/usr/bin/env python

#Exercise 1

d= dict(name= u"Chris", city= u"Seattle", cake= u"Chocolate")

def show(d):
    for i, j in d.items():
        print "%s: %s" % (i, j)

show(d)

del d["cake"]
show(d)

d["fruit"]= u"Mango"

print d.keys(), "\n", d.values()

print "cake" in d.keys()
print "Mango" in d.values()

#Exercise 2

hexd= {}
nums= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
dexnums= [1, 2, 3, 4, 5, 6, 7, 8, 9, u'A', u'B', u'C', u'D', u'E', u'F']

for i, j in zip(nums, dexnums):
    hexd[i] = j

show(hexd)

for i, j in d.items():
    d[i]= j.count(u'a')

show(d)

#Exercise 3:

s2 = set([x for x in range(21) if x%2== 0])
s3 = set([x for x in range(21) if x%3== 0])
s4 = set([x for x in range(21) if x%4== 0])

for i in [s2, s3, s4]:
    print "\n"
    for j in i:
        print j,

print "\n"
print s3.issubset(s2)
print s4.issubset(s2)

#Exercise 5

s= set(list(u'Python'))
s.add(u'i')

for i in s:
    print i,

print "\n"

fs = frozenset(list(u'marathon'))

for i in fs:
    print i,
print "\n"

union= fs.union(s)
intersection= fs.intersection(s)

print "Union: " + ", ".join(list(union))
print "Intersection: " + ", ".join(list(intersection))


