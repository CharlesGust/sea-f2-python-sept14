def fibonacci(n):
    """Compute Fibonacci's number from input value."""
    #0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
    if n == 0: return 0
    elif n == 1 or n == 2: return n - 1
    else: return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(nth):
    """Compute Lucas's number from input value."""
    #2, 1, 3, 4, 7, 11, 18, 29, 47, 76...
    if nth == 0: return 0
    elif nth == 1: return nth + 1
    elif nth == 2: return nth - 1
    else: return lucas(nth - 1) + lucas(nth - 2)

def sum_series(x, fib1=0, fib2=1):
    """Compute value (X,y,z) in sum series with designated starting numbers (x,Y,Z)."""
    if x == 0: return 0
    elif x == 1: return fib1
    elif x == 2: return fib2
    else:
        return sum_series(x - 1, fib1, fib2) + sum_series(x - 2, fib1, fib2)


if __name__ == "__main__":
    #Tests Fibonacci function to ensure accuracy in computations
    assert fibonacci(0) == 0
    assert fibonacci(1) == 0
    assert fibonacci(5) == 3
    assert fibonacci(13) == 144
    #Tests Lucas function to ensure accuracy in computations
    assert lucas(0) == 0
    assert lucas(1) == 2
    assert lucas(5) == 7
    assert lucas(11) == 123
    #Tests Sum Series function to ensure accuracy in computations
    assert sum_series(0) == 0
    assert sum_series(13) == 144
    assert sum_series(1,2,1) == 2
    assert sum_series(5,2,1) == 7
    #Prints message affirming accuracy
    print "All tests pass."