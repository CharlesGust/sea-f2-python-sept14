#!/usr/bin/env python

#Exercise 1
print "EXERCISE 1"
fruit = [u'apples', u'pears' , u'oranges', u'peaches']

print fruit

fruit.append(raw_input(u"What else would you like to add?  "))

print fruit

i = int(raw_input(u"Pick a number between 1 and %i:  " % len(fruit)))

suff = [u'st', u'nd', u'rd'][i - 1] if i in (1, 2, 3) else "th"

print "The %i%s kind of fruit is: %s" % (i, suff, fruit[i - 1])

fruit = [u'bananas'] + fruit

print fruit

fruit.insert(0, u'plumbs')

print fruit

for f in fruit:
    if f[0] == "p":
        print f

#Exercise 2
print "EXERCISE 2"
fruit = [u'apples', u'pears', u'oranges', u'peaches']
print fruit

fruit.pop()

print fruit

rmfruit = raw_input("What fruit do you dislike: ").lower()

if rmfruit in fruit:
    fruit.remove(rmfruit)
else:
    print "You do not have any %s" % rmfruit

#BONUS
print "BONUS"
fruit = [u'apples', u'pears', u'oranges', u'peaches']
print fruit

doublefruit = fruit * 2
print doublefruit

def rem_all_occur(x, lst):
    while x in lst:
        lst.remove(x)
    return lst

rmfruit = raw_input(u"What fruit do you dislike?  ").lower()

if rmfruit in fruit:
    print rem_all_occur(rmfruit, doublefruit)
else:
    print u"%s isn't a fruit that you have." % rmfruit

#Exercise 3
print "EXERCISE 3"
fruit = [u'apples', u'pears', u'oranges', u'peaches']
print fruit

for f in fruit[:]:
    answer = raw_input(u"Do you like %s?  " % f).lower()
    while answer not in [u'yes', u'no']:
        answer = raw_input(u"Please type 'yes' or 'no'." ).lower()
    if answer == "no":
        fruit.remove(f)

print fruit

#Excercise 4
print "EXERCISE 4"

fruit = [u'apples', u'pears', u'oranges', u'peaches']
print fruit

clone = fruit[:]

for i in range(len(fruit)):
    clone[i] = list(clone[i])
    clone[i].reverse()
    clone[i] = "".join(clone[i])

fruit.pop()

print clone, "\n", fruit

