def function_builder(x=0):
    s = {}
    for i in range(x):
        print i
        s[i] = lambda : 2 + 2
        print s[i]
    print s
