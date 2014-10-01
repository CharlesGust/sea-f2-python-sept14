#!/usr/bin/env python

#PART 1
fruits = ["Apples", "Pears", "Oranges", "Peaches"]
print fruits
fruits.append(raw_input("What fruit would you like to add to the list? > "))
print fruits
add_fruit = int(raw_input("Please enter a number. > "))
print "You entered: %i, %s" % (add_fruit, fruits[add_fruit-1])
add_fruit = [raw_input("Please enter a fruit to add to the list. > ")]
fruits = add_fruit + fruits
print fruits
fruits.insert(0, raw_input("Please enter a fruit to add to the list. > "))
print fruits
print "These fruits start with 'P'"
for fruit in fruits:
    if fruit[0] == "P":
        print fruit

#PART 2
print fruits
print "I don't like %s." % fruits.pop(-1)
print fruits

fruits = fruits * 2
print fruits
user_inp = raw_input("What fruit would you like to remove all of? > ")
while user_inp not in fruits:
    print "That fruit is not in the list."
    user_inp = raw_input("What fruit would you like to remove all of? > ")
while user_inp in fruits:
    fruits.remove(user_inp)
print fruits

#PART 3
for fruit in fruits[:]:
    print fruits
    user_inp = raw_input("Do you like %s? > " % fruit.lower())
    while user_inp.lower() != "no" and user_inp.lower() != "yes":
        print "%s is an invalid answer." % user_inp
        user_inp = raw_input("Do you like %s? > " % fruit.lower())
    if user_inp.lower() == "no":
        fruits.remove(fruit)
    elif user_inp.lower() == "yes":
        pass

#PART 4
print fruits
fruits_copy = []
for fruit in fruits:
    f = fruit[::-1]
    fruits_copy.append(f)

fruits.pop(-1)
print "Original fruits: %s" % fruits
print "Fruits copy: %s" % fruits_copy