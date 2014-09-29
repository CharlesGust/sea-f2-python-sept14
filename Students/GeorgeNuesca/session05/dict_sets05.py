# PART 1
food_prefs = {u'name' : u'Chris',
u'city' : u'Seattle',
u'cake' : u'chocolate',
u'fruit' : u'mango',
u'salad' : u'greek',
u'pasta' : u'lasagna'}

print '{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and {pasta} pasta'.format(**food_prefs)

# PART 2: Zipping making a dictionary from two lists.
hexades = range(16)
print dict(zip(range(16), [hex(hexade) for hexade in hexades]))

# PART 3: Counting a specific item in values of a key
print {i : hex(i) for i in range(16)}

# PART 4

# for k, v in food_prefs.iteritems():
#     food_prefs[k] = v.count('a')

food_prefs = {k : v.count('a') for k, v in food_prefs.iteritems()}
print food_prefs

# PART 5
s2 = range(21)
print [s for s in s2 if s % 2 == 0]

s3 = range(21)
print [s for s in s3 if s % 3 == 0]

s4 = range(21)
print [s for s in s4 if s % 4 == 0]

loop in loop

