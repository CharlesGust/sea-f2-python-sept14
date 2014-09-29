biography = {u"name": u"Chris", u"city": u"Seattle", u"cake": u"Chocolate"}

print biography

biography.pop(u"cake")

print biography

biography.setdefault(u"fruit", u"Mango")

print biography

print biography.keys()

print biography.values()

print biography.has_key(u"cake")

print u"Mango" in biography.values()

# Part 2
decimals = range(16)
hexes = decimals[:]
for index, num in zip(decimals,hexes):
    hexes[index] = hex(num)

print dict(zip(decimals, hexes))

# Part 3
biography_acount = {}
for key in biography:
    biography_acount[key] = biography[key].count(u"a")

print biography, biography_acount

# Part 4
s2, s3, s4 = set(), set(), set()

for i in range(21):
    if i % 4 == 0:
        s2.add(i)
        s4.add(i)
    elif i % 2 == 0:
        s2.add(i)
    if i % 3 == 0:
        s3.add(i)

print s2, s3, s4
print s3.issubset(s2)
print s4.issubset(s2)

# Part 5
pyset = set(u"Python")
pyset.add(u'i')
print pyset

frozenmarathon = frozenset(u"marathon")
print frozenmarathon
print frozenmarathon.union(pyset)
print frozenmarathon.intersection(pyset)
