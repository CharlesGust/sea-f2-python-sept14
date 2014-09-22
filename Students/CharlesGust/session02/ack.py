def Ackermann(m, n):
    """return Ackermann function for demonstrating exponential recursive"""
    if (m < 0) or (n < 0):
        return None
    if m == 0:
        return n+1
    if n == 0:
        return Ackermann(m-1, 1)
    return Ackermann(m-1, Ackermann(m, n-1))

"""
Ackermann( 0 , 0 ) =  1
Ackermann( 0 , 1 ) =  2
Ackermann( 0 , 2 ) =  3
Ackermann( 0 , 3 ) =  4
Ackermann( 0 , 4 ) =  5
Ackermann( 1 , 0 ) =  2
Ackermann( 1 , 1 ) =  3
Ackermann( 1 , 2 ) =  4
Ackermann( 1 , 3 ) =  5
Ackermann( 1 , 4 ) =  6
Ackermann( 2 , 0 ) =  3
Ackermann( 2 , 1 ) =  5
Ackermann( 2 , 2 ) =  7
Ackermann( 2 , 3 ) =  9
Ackermann( 2 , 4 ) =  11
Ackermann( 3 , 0 ) =  5
Ackermann( 3 , 1 ) =  13
Ackermann( 3 , 2 ) =  29
Ackermann( 3 , 3 ) =  61
Ackermann( 3 , 4 ) =  125
"""
if __name__ == "__main__":
    verify = True
    verify = verify and Ackermann(0, 0) == 1
    verify = verify and Ackermann(0, 1) == 2
    verify = verify and Ackermann(0, 2) == 3
    verify = verify and Ackermann(0, 3) == 4
    verify = verify and Ackermann(0, 4) == 5
    verify = verify and Ackermann(1, 0) == 2
    verify = verify and Ackermann(1, 1) == 3
    verify = verify and Ackermann(1, 2) == 4
    verify = verify and Ackermann(1, 3) == 5
    verify = verify and Ackermann(1, 4) == 6
    verify = verify and Ackermann(2, 0) == 3
    verify = verify and Ackermann(2, 1) == 5
    verify = verify and Ackermann(2, 2) == 7
    verify = verify and Ackermann(2, 3) == 9
    verify = verify and Ackermann(2, 4) == 11
    verify = verify and Ackermann(3, 0) == 5
    verify = verify and Ackermann(3, 1) == 13
    verify = verify and Ackermann(3, 2) == 29
    verify = verify and Ackermann(3, 3) == 61
    verify = verify and Ackermann(3, 4) == 125
    if verify:
        print "All Tests Pass"

    """
    for m in xrange(0, 4):
        for n in xrange(0, 5):
            print "Ackermann(", m, ",", n, ") = ", Ackermann(m, n)
    """
