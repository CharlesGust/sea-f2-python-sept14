#!/usr/bin/env python

def function_builder(n=10):
    return [lambda i, inc=j: i + inc for j in range(n)]

if __name__ == '__main__':
    the_list = function_builder(4)
    ### so the_list should contain n functions (callables)
    assert the_list[0](2) == 2
    ## the zeroth element of the list is a function that add 0
    ## to the input, hence called with 2, returns 2
    assert the_list[1](2) == 3
    ## the 1st element of the list is a function that adds 1
    ## to the input value, thus called with 2, returns 3
    print "All Tests Pass"
    print "Printing f(5) for all 4 functions, should be 5,6,7,8"
    for f in the_list:
        print f(5)
