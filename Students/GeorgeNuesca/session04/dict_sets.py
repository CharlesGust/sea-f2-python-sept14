# Part 1
dessert = {u'name' : u'Chris', u'city' : u'Seattle', u'Cake' : u'chocolate'}
print dessert

dessert.pop(u'Cake', None)
print dessert

dessert[u'fruit'] = u'Mango'
print dessert

print dessert.keys()
print dessert.values()

print u'cake' in dessert.keys()
print u'Mango' in dessert.values()

# Part 2: Zipping making a dictionary from two lists.
numbers = range(0, 16)
hexades = range(0, 16)
for i, hexade in enumerate(hexades):
    hexades[i] = hex(hexade)
numhexs = dict(zip(numbers, hexades))
print numhexs

# Part 3: Counting a specific item in values of a key
for key in dessert:
    dessert[key] = dessert[key].count(u'a')
print dessert

# Part 4
s2 = set(range(20))
for s in s2.copy():
    if s % 2 == 0:
        continue
    else:
        s2.remove(s)
s2 = set(s2)

s3 = set(range(20))
for s in s3.copy():
    if s % 3 == 0:
        continue
    else:
        s3.remove(s)
s3 = set(s3)

s4 = set(range(20))
for s in s4.copy():
    if s % 4 == 0:
        continue
    else:
        s4.remove(s)

print 'Set divible by 2: ', s2  #A way to get rid of set during printing?
print 'Set divible by 3: ', s3
print 'Set divible by 4: ', s4

print 'Is s3 a subset of s2: ', s3.issubset(s2)
print 'Is s4 a subset of s2: ', s4.issubset(s2)

# Part 5
s1 = set('Python')
s1.add('i')

s2 = frozenset('marathon')

print s1.union(s2)
print s1.intersection(s2)