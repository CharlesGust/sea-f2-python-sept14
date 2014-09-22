def fibonacci(n):
    """Return the nth number in the Fibonacci sequence (starting at 0, F_0 = 0, F_1 = 1)"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
    """Return the nth number in the Lucas sequence (starting at 0, L_0 = 2, L_1 = 1)"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return 2
    if n == 1:
        return 1
    return lucas(n - 1) + lucas(n - 2)

def sum_series(n, numZero = 0, numOne = 1):
    """Return the nth number in a sum series like the Fibonacci sequence starting with numZero and numOne"""
    if n < 0:
        return None #bad input, throw error maybe
    if n == 0:
        return numZero
    if n == 1:
        return numOne
    return sum_series(n - 1, numZero, numOne) + sum_series(n - 2, numZero, numOne)

if __name__ == '__main__':
    #Tests first several values of the Fibonacci sequence
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

    #Tests first several values of the Lucas sequence
    assert lucas(0) == 2
    assert lucas(1) == 1
    assert lucas(2) == 3
    assert lucas(3) == 4
    assert lucas(4) == 7
    assert lucas(5) == 11
    assert lucas(6) == 18
    assert lucas(7) == 29
    assert lucas(8) == 47
    assert lucas(9) == 76
    assert lucas(10) == 123
    assert lucas(11) == 199
    assert lucas(12) == 322
    assert lucas(13) == 521
    assert lucas(14) == 843

    #Verify that sum_series(n) without optional arguments is fibonacci(n)
    for i in range(25):
        assert sum_series(i) == fibonacci(i)
    #Verify that sum_series(n,2,1) with optional arguments 2, 1 is lucas(n)
    for i in range(25):
        assert sum_series(i,2,1) == lucas(i)
    #Verify some simple behaviors of sum_series(...)
    for i in range(25):
        assert sum_series(0,i,i+1) == i
        assert sum_series(1,i+1000,i) == i
        assert sum_series(i, 1, 1) == fibonacci(i+1)
        assert sum_series(i, 3, 4) == lucas(i+2)


    print "All Tests Pass"
