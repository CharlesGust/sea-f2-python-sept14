"""
ackermann funciton
"""

def ack(m, n):
    if m == 0:
        n+= 1
    elif m > 0:
        if n == 0:
            return ack(m-1, 1)
        elif n > 0:
            return ack(m-1, ack(m, n-1))
    return n

if __name__ == "__main__":
    for m in range(4):
        for n in range(4):
            print (m, n), ":", ack(m, n)
            print "All Tests Pass"
