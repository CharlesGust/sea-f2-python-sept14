#!/usr/bin/python

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals', 'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]

# What is the output of:

print comprehension[0]
# ???

print comprehension[2]
# ???

# (figure it out before you try it)

#   Filtering lists with list comprehensions

feast = ['spam', 'sloths', 'orangutans', 'breakfast cereals',
         'fruit bats']

comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

# What is the output of:

print len(feast)
# ???

print len(comprehension)
# ???

# (figure it out first!)

#    Unpacking tuples in list comprehensions

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]

comprehension = [skit * number for number, skit in list_of_tuples]

# What is the output of:

print comprehension[0]
# ???

print len(comprehension[2])
# ???

#   Double list comprehension

list_of_eggs = ['poached egg', 'fried egg']

list_of_meats = ['lite spam', 'ham spam', 'fried spam']

comprehension = ['{0} and {1}'.format(egg, meat)
                 for egg in list_of_eggs for meat in list_of_meats]

# What is the output of:

print len(comprehension)
# ???

print comprehension[0]
# ???

#    Creating a set with set comprehension

comprehension = {x for x in 'aabbbcccc'}

# What is the output of:

print comprehension
# ???

#    Creating a dictionary with dictionary comprehension

dict_of_weapons = {
    'first': 'fear',
    'second': 'surprise',
    'third': 'ruthless efficiency',
    'forth': 'fanatical devotion',
    'fifth': None}

dict_comprehension = {k.upper(): weapon
                      for k, weapon in dict_of_weapons.iteritems() if weapon}

# What is the output of:


print 'first' in dict_comprehension
#        ???

print 'FIRST' in dict_comprehension
# ???

print len(dict_of_weapons)
# ???

print len(dict_comprehension)
# ???
