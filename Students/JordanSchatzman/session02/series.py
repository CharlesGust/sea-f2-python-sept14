#!/usr/bin/env python
import sys

def fibonacci(n):
    """This function returns the nth value of the Fibonacci series"""
    if n < 3:
        return n-1
    return fibonacci(n-2) + fibonacci(n-1)
    
def lucas(m):
    """This function returns the nth value of the Lucas series"""
    if m == 1:
        return 2
    elif m == 2:
        return 1
    return lucas(m-2) + lucas(m-1)

def sum_series(a, b = 0, c = 1):
    """This function returns the nth value of a user defined series"""
    if a == 1:
        return b
    elif a == 2:
        return c
    return sum_series(a-2, b, c) + sum_series(a-1, b, c)

if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    c = int(sys.argv[3])
    # Make sure fibonacci function works properly
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(3) == 1
    assert fibonacci(4) == 2
    assert fibonacci(5) == 3
    assert fibonacci(6) == 5
    # Make sure lucas function works properly
    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(3) == 3
    assert lucas(4) == 4
    assert lucas(5) == 7
    assert lucas(6) == 11
    # Make sure sum_series function works properly
    assert sum_series(1) == fibonacci(1)
    assert sum_series(2) == fibonacci(2)
    assert sum_series(3) == fibonacci(3)
    assert sum_series(1,2,1) == lucas(1)
    assert sum_series(2,2,1) == lucas(2)
    assert sum_series(3,2,1) == lucas(3)
    #Print output of sum_series function
    print sum_series(a,b,c)