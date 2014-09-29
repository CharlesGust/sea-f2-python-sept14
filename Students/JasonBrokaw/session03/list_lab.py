#!/usr/local/bin/python


# SERIES 1
fruits = [u"Apples", u"Pears", u"Oranges", u"Peaches"]

print fruits

new_fruit = raw_input(u"Type a fruit: ")

fruits.append(new_fruit)

print fruits

index = int(raw_input(u"Type an index from 1 through %i: " % len(fruits)))

print "Item %i in the list is %s" % (index, fruits[index - 1])

fruits = [u"Cantaloupe"] + fruits

print fruits

fruits.insert(0, u"Banana")

print fruits

for fruit in fruits:
    if fruit[0] == "P":
        print fruit

# SERIES 2
print "BEGINNING SERIES 2"
fruits2 = fruits[:]

print fruits2

fruits2.pop()

print fruits2

fruits2 = 2 * fruits2

print fruits2

fruit_to_delete = raw_input(u"Type a fruit to delete from the list: ")

while True:
    try:
        fruits2.index(fruit_to_delete)
        break
    except ValueError:
        fruit_to_delete = raw_input(u"That fruit wasn't in the list. Try again: ")

while True:
    try:
        fruits2.remove(fruit_to_delete)
    except ValueError:
        break

print fruits2

# SERIES 3
print "BEGINNING SERIES 3"

fruits3 = fruits[:]

print fruits3

for fruit in fruits3[:]:
    like = raw_input(u"Do you like %s (yes/no)? " % fruit.lower()).lower()
    while (like != "yes") and (like != "no"):
        print u"Please type 'yes' or 'no'"
        like = raw_input(u"Do you like %s (yes/no)? " % fruit.lower()).lower()
    if like == u"no":
        fruits3.remove(fruit)

print fruits3

# SERIES 4
print "BEGINNING SERIES 4"

fruits4 = fruits[:] #I'm just considering fruits to be the original list here

i = 0
for fruit in fruits4[:]:
    list_fruit = list(fruit)
    list_fruit.reverse()
    fruits4[i] = u"".join(list_fruit)
    i = i + 1

fruits.pop()

print fruits, fruits4
