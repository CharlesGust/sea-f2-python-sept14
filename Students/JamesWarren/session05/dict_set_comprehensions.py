#!/usr/bin/env python

#PART 1
d = {
    'name' : 'Chris',
    'city' : 'Seattle',
    'cake' : 'chocolate',
    'fruit' : 'mango',
    'salad' : 'greek',
    'pasta' : 'lasagna'
}

print "{name} is from {city}, and he likes {cake} cake, {fruit} fruit, \
{salad} salad, and {pasta} pasta.".format(**d)


#PART 2
d1 = [range(0,16)]
d2 = [hex(x) for x in range(0,16)]

#PART 3
d3 = {k:hex(k) for k in range(16)}

#PART 4
new_dict = {k:v.count('a') for k, v in d.iteritems()}
print new_dict

#PART 5
s2 = {s for s in range(20) if not s%2}
s3 = {s for s in range(20) if not s%3}
s4 = {s for s in range(20) if not s%4}
print "s2: %s" % s2
print "s3: %s" % s3
print "s4: %s" % s4

for f in range(2,5):
    sx = {s for s in range(20) if not s%f}
    print "sx%i: %s" % (f, sx)
