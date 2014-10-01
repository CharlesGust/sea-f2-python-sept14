#!/usr/bin/env python

#Exercise 1
food_prefs= {u'name': u'Chris', u'city': u'Seattle', u'cake': u'chocolate',\
u'fruit': u'mango', u'salad': u'Greek', u'pasta': u'lasagna'}

s= u"{name} is from {city}, and he likes {cake} cake, {fruit} fruit, {salad} salad, and\
 {pasta} pasta".format(**food_prefs)

print s

#Exercise 2
hexdict= dict([(i, hex(i)) for i in range(16)])

#Exercise 3
hexdict1= {i: hex(i) for i in range(16)}

#Exercise 4
num_a= food_prefs.copy()

for x in food_prefs.keys():
    num_a[x]= food_prefs[x].count(u'a')

#Exercise 5

#a)
s2= {x for x in range(21) if x % 2==0}
s3= {x for x in range(21) if x % 3==0}
s4= {x for x in range(21) if x % 4==0}

#b)
def set_builder(n):
    s= []
    for i in range(1, n+1):
        s.append({x for x in range(21) if not x%i})
    return s

#c)
def set_more_buildier(n):
    return [{x for x in range(21) if not x%i} for i in range(1, n+1)]