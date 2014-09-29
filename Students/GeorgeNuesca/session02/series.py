# Starting from n = 1, not n = 0 for first element

def  fib(n):
    """Calculates the nth term in a Fibonacci series starting at n = 1 for the first element."""
    if n == 1 or n == 2:
        return n - 1
    elif n > 2:
        n = n + 1
        return fib(n - 2) + fib(n - 3)
    else:
        return None

def lucas(n):
    """Calculates the nth term in a Lucas series starting at n = 1 for the first element."""
    if n == 1:
        return 2
    elif n == 2:
        return 1
    elif n > 2:
        n = n + 1
        return lucas(n - 2) + lucas(n - 3)
    else:
        return None

def sum_series(n, x = 0, y = 1):
    """Calculate the nth term in a series with parameters (n, x, y), where x and y are the
     first 2 numbers of the series. The first element starts with n = 1."""
    if n == 1:
        return x
    elif n == 2:
        return y
    elif n > 2:
        n = n + 1
        return sum_series(n - 2, x, y) + sum_series(n - 3, x, y)
    else:
        return None


if __name__ == '__main__':
    assert fib(1) == 0
    assert fib(2) == 1
    assert fib(3) == 1
    assert fib(4) == 2
    assert fib(5) == 3
    assert fib(6) == 5
    assert fib(7) == 8
    assert fib(8) == 13
    assert fib(9) == 21
    assert fib(10) == 34

    assert lucas(1) == 2
    assert lucas(2) == 1
    assert lucas(3) == 3
    assert lucas(4) == 4
    assert lucas(5) == 7
    assert lucas(6) == 11
    assert lucas(7) == 18
    assert lucas(8) == 29
    assert lucas(9) == 47
    assert lucas(10) == 76

    assert sum_series(1) == 0
    assert sum_series(2) == 1
    assert sum_series(6) == 5
    assert sum_series(10) == 34
    assert sum_series(1, 2, 1) == 2
    assert sum_series(2, 2, 1) == 1
    assert sum_series(6, 2, 1) == 11
    assert sum_series(10, 2, 1) == 76
    assert sum_series(1, 1, 1) == 1
    assert sum_series(2, 1, 1) == 1
    assert sum_series(3, 1, 1) == 2
    assert sum_series(4, 1, 1) == 3
    assert sum_series(5, 1, 1) == 5
    assert sum_series(6, 1, 1) == 8
    assert sum_series(1, 3, 5) == 3
    assert sum_series(2, 3, 5) == 5
    assert sum_series(3, 3, 5) == 8
    assert sum_series(4, 3, 5) == 13
    assert sum_series(5, 3, 5) == 21
    assert sum_series(6, 3, 5) == 34

    print "TEST CASES PASSED"