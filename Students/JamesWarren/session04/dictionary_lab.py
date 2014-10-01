#!/usr/bin/env python

#PART 1
d = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'Chocolate'
}
print d
del d['cake']
print d
d['fruit'] = 'Mango'

print d.keys()
print d.values()

print 'cake' in d
print 'Mango' in d.values()

#PART 2
d1 = {}
d2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
d3 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
for k, v in zip(d2, d3):
    d1[k] = v

#PART 3
new_dict = {}

for key, value in d.iteritems():
    new_dict[key] = value.count(u'a')

print new_dict

#PART 4
s2 = set([0,2,4,6,8,10,12,14,16,18,20])
s3 = set([0,3,6,9,12,15,18])
s4 = set([0,4,8,12,16,20])

print s3.issubset(s2)
print s4.issubset(s2)

#PART 5
piset = set('Python')
piset.update('i')

marset = frozenset(('marathon'))

print marset.union(piset)
print marset.intersection(piset)