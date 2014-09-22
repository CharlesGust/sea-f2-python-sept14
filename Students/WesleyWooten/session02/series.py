"""
Fibonacci and Lucas Series functions
"""

def fibonacci(n):
    """ Returns the nth number in the fibonacci series """
    if n<2: return n
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
    """ Returns the nth number in the Lucas series """
    if n==0: return 2
    elif n==1: return n
    return lucas(n-1) + lucas(n-2)

if __name__ == "__main__":
    for x in range(10): print fibonacci(x)
    for x in range(10): print lucas(x)
