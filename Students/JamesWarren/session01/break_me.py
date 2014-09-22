#NameError################
#Mary is undefined, causing Name Error (to fix, turn Mary into string)
def names(name):
    if name == Mary:
        print "Hi Mary!"

names("Linda")


#TypeError################
#Cannot combine int and string, causing Type Error
def types(a, b):
    if a < b:
        return a + b

types(7, "Fred")


#SyntaxError###############
#"is ==" is invalid, causing Syntax Error (remove "is" to fix)
def syntax(n):
    if n is == "John":
        return True

syntax("Joe")


#AttributeError#############
#int does not have .lower() property, causing Attribute Error
def attributes(k):
    return k.lower()

attributes(17)
