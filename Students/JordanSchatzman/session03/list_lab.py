#!/usr/bin/env python
import sys


Fruits = ["Apples", "Pears", "Oranges", "Peaches"]

def fruitfun(Fruits):
    """Execute Series 1"""
    print Fruits
    newfruit1 = raw_input('Add New Fruit :')
    Fruits.append(newfruit1)
    print Fruits
    fruitnum = int(raw_input('Which Fruit do you Want?'))
    print Fruits[fruitnum-1]
    Fruits = ['Starfruit'] + Fruits
    Fruits.insert(0, 'Banana')
    print Fruits
    for i in range(len(Fruits)):
        if Fruits[i][0].upper() == 'P':
            print Fruits[i]
    return Fruits

def fruitfun2(Fruits):
    """Execute Series 2"""
    Fruits2 = Fruits[:]
    print "Begin Series 2" 
    print Fruits2
    Fruits2.pop()
    print Fruits2
    removefruit = raw_input('Remove Fruit :')
    Fruits2.remove(removefruit)
    print Fruits2
    return Fruits2


def fruitfun3(Fruits):
    """Execute Series 3"""
    Fruits3 = Fruits[:]
    print "Begin Series 3"
    print Fruits3
    for i in Fruits3 :
        likefruit = raw_input("Do you like %s? :"%i.lower())
        while likefruit != u"yes" and likefruit !=u"no" :
            print u"You must give a yes or no answer \n"
            likefruit = raw_input("Do you like %s? :"%i.lower())
        if likefruit == u"no" :
            Fruits3.remove(i)
    print Fruits3
    return Fruits3

    
def fruitfun4(Fruits):
    """Execute Series 4"""
    Fruits4 = []
    print "Begin Series 4"
    for i in Fruits:
        Fruits4.append(i[::-1])
    print Fruits4
    Fruits.pop()
    print Fruits
    return Fruits4
    


if __name__ == "__main__":
    fruitfun(Fruits)
    fruitfun2(Fruits)
    fruitfun3(Fruits)
    fruitfun4(Fruits)