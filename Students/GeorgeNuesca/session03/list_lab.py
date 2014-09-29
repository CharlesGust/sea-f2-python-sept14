#!/usr/bin/env python2.7

# PART 1: Adding fruit to list and listing fruit with first letter "P" or "p".
fruitlist1 = ["Apples","Pears","Orange","Peaches"]
print fruitlist1

addfruit1 = raw_input('Please add another fruit to the list: ')
fruitlist1.append(addfruit1)
print fruitlist1

locfruit = int(raw_input('Please enter a number: '))
print fruitlist1[locfruit - 1]

addfruit2 = [raw_input('Please add a second fruit to the list: ')]
fruitlist1 = addfruit2 + fruitlist1
print fruitlist1

addfruit3 = raw_input('Please add a third fruit to the list: ')
fruitlist1.insert(0, addfruit3)
print fruitlist1

for fruit in fruitlist1:
    if fruit[0] in ['p', 'P']:
        print fruit

fruitlist1 = tuple(fruitlist1)


# PART2: Removing fruit from list in PART1.
fruitlist2 = list(fruitlist1)
print fruitlist2
fruitlist2.pop()
print fruitlist2
fruitremoval = raw_input('Specify a fruit to remove from the list: ')
fruitlist2.remove(fruitremoval)
print fruitlist2


# PART3: Makes fruitlist1 lowercase and asks user to remove a fruit.
fruitlist3 = list(fruitlist1)
print fruitlist3
for i, fruit in enumerate(fruitlist3):
    fruitlist3[i] = fruit.lower()

for fruit in fruitlist3[:]:
    response = raw_input('Do you like %s? (y/n)' % fruit)
    while response not in ['y', ' n']:
        if response in ['y', 'n']:
            break
        response = raw_input('Type "y" or "n": ')
    if response == 'n':
        fruitlist3.remove(fruit)
print fruitlist3


#PART4: Reverses letters for each string and removes last element in list.
fruitlist4 = list(fruitlist1)
for i, fruit in enumerate(fruitlist4):
    fruitlist4[i] = fruit[::-1]
fruitlist4.pop()
print fruitlist1
print fruitlist4