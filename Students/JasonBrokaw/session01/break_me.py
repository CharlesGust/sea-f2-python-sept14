def throwName():
    '''Throws a NameError'''
    print b

def throwType():
    '''Throws a TypeError'''
    print "a" + 5

# def throwSyntax():
#     '''Throws a SyntaxError'''
#     if a < 6
#         print a

def throwAttribute():
    '''Throws an AttributeError'''
    a = 6
    print a.length

# throwName()
# throwType()
# throwAttribute()
