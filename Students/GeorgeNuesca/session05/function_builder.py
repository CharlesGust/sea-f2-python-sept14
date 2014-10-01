def function_builder(x=0):
    s = {}
    for i in range(x):
        s[i] = lambda y, j = i:  j + y  # j assigned at function definition time only (kwarg)
    return s