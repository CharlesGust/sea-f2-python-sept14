#!/usr/env/python

x = ['Apples','Pears','Oranges', 'Peaches']
print x
y = raw_input("Add another fruit?\n: ")
x.append(y)
print x

indexnum = raw_input("Display fruit at bin number (Starting at 1): ")
print indexnum, x[int(indexnum)- 1]

x = x + ['Guavas']
print x

x.insert(0, 'Lemons')
print x

for i in range(len(x)):
    temp = x[i]
    if temp[0] == 'P':
        print temp

print x
x.pop()
print x

delete = raw_input("Enter a fruit to delete\n: ")
x.remove(delete)
print x
for i in x:
	fruit = i.lower()
	deletelist = []
	question = "Do you like %s? \n: " % fruit
	answer = raw_input(question)
	if answer == 'no':
		deletelist.append(i)
	while answer != 'yes' and answer != 'no':
		answer = raw_input("Please answer 'yes' or 'no'\n: ")
for fruit in deletelist:
	x.remove(fruit)
print x

newx = x[:]

for i in range(len(newx)):
	newx[i] = newx[i][::-1]

x.pop()
print x
print newx



