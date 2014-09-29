#!/usr/env/python
def series_1():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print fruits

    add_fruit = raw_input("Think of another fruit not listed: ")
    fruits.append(add_fruit)
    print fruits

    pick_num = raw_input("Pick a number: ")
    print pick_num + " corresponds to: " + fruits[int(pick_num) - 1]

    add_fruit = [raw_input("Think of another fruit: ")]
    fruits = add_fruit + fruits
    print fruits

    add_fruit = raw_input("One last fruit to add: ")
    fruits.insert(0, add_fruit)
    print fruits

    list_fruits = []
    for fruit in fruits:
        if fruit[0] == "P":
            list_fruits.append(fruit)
    print list_fruits

def series_2():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    print fruits

    fruits.pop()
    print fruits

    remove_fruit = raw_input("Pick a fruit to remove: ")
    fruits.remove(remove_fruit)
    print fruits

def series_3():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    for fruit in fruits[:]:  
        answer = '' 
        while answer.lower() != 'no' or answer.lower() != 'yes':
            answer = raw_input("Do you like %s?: " % fruit)
            if answer.lower() == 'yes' or answer.lower() == 'no':
                break 
            else:
                answer = raw_input('Say yes or no: ')
        if answer.lower() == 'no':
            fruits.remove(fruit)
        elif answer.lower() == 'yes':
            print "You like %s" % fruit

def series_4():
    fruits = ["Apples", "Pears", "Oranges", "Peaches"]
    reverse_fruits = []
    for fruit in fruits:
        reverse_fruits.append(fruit[::-1])
    print reverse_fruits
    fruits.pop()
    print fruits

