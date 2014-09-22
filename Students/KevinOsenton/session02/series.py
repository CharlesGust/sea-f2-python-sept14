def fibonacci(n):
    """Return nth position of the Fibonacci series"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """Return nth position of the Lucas series"""
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2)

def sum_series(n, value = 0):
    """Return nth position of either Fibonacci or Lucas series"""
    #Default at Fibonacci
    if n == 0:
        return value
    elif n == 1:
        return 1
    else:
        return sum_series(n-1, value) + sum_series(n-2, value)

if __name__ == '__main__':
    #Test for Fibonacci
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    print "All Fibonacci Tests Passed"

    #Test for Lucas
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    print "All Lucas Tests Passed"
    
    #Test for sum_series (Fibonacci)
    assert sum_series(0) == 0
    assert sum_series(1) == 1 
    assert sum_series(2) == 1
    assert sum_series(3) == 2
    assert sum_series(4) == 3
    assert sum_series(5) == 5
    print "All sum_series (Fibonacci) Tests Passed"

    #Test for sum_series (Lucas)
    assert sum_series(0, 2) == 2
    assert sum_series(1, 2) == 1
    assert sum_series(2, 2) == 3
    assert sum_series(3, 2) == 4
    assert sum_series(4, 2) == 7
    assert sum_series(5, 2) == 11
    print "All sum_series (Lucas) Tests Passed"




