def ack(m, n):
    """Computes the Ackerman algorithm for ack(m,n)"""

    if m < 0 or n < 0:
        return None
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ack(m - 1, 1)
    if m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

if __name__ == '__main__':
	print 'running as main'
	assert ack(1,2) == 4
	assert ack(2,3) == 9
	assert ack(3,4) == 125
