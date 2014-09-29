def ExcNameError1():
    KeyserSoze

def ExcNameError2():
    KeyserSoze()


def ExcTypeError1():  #Type errors
    a =  u"tough"
    sum([a, a, a])  #Builtin can not sum strings

def ExcTypeError2():
    sum = (5*5)
    b = 2
    return sum([b, b])  #Sum is a rebound?rebinded? symbol and can no longer sum int values


def ExcAttributeError():
    c = 1000 % 999
    c.capitalize()
    return c


#def ExcSyntaxError1():
#    count = 0
#    for i in range(3):
#        count += 1
#    return count