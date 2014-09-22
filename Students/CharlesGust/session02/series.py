def sum_series(n, seed1=0, seed2=1):
    """ return the nTH number of series seeded with seed1 and seed2 """
    if n <= 2:
        if n == 1:
            return seed1
        elif n == 2:
            return seed2
        else:
            return None
    return sum_series(n-1, seed1, seed2) + sum_series(n-2, seed1, seed2)


def lucas(n):
    """ return the nTH Lucas number """
    return sum_series(n, 2, 1)


def fibonacci(n):
    """ return the nTH Fibonacci number """
    return sum_series(n)


if __name__ == "__main__":
    """ check fibonacci base cases """
    assert(fibonacci(1) == 0)
    assert(fibonacci(2) == 1)

    """ check lucas base cases """
    assert(lucas(1) == 2)
    assert(lucas(2) == 1)

    """ check that invalid values return None """
    assert(sum_series(0) is None)
    assert(sum_series(-1) is None)
