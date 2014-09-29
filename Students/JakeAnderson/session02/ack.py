# coding: utf-8
#ack program with the ackermann_function

""" ackermann_function """
def ack(m,n):
    #n+1   if  m = 0
    if m is 0:
    	return n + 1
    #A(m−1, 1)   if  m > 0  and  n = 0 
    if m > 0 and n is 0:
    	return ack(m-1, 1)
    #A(m−1, A(m, n−1))   if  m > 0  and  n > 0
    if m > 0 and n > 0:
    	return ack(m-1, ack(m, n - 1))

if __name__ == "__main__":
	expected = [[1,2,3,4,5],
				[2,3,4,5,6],
				[3,5,7,9,11],
				[5,13,29,61,125]]
	ok = True
	for m in range(4):
		for n in range(5):
			actual = ack(m,n)
			if not actual == expected[m][n]:
				print "error"
				ok = False
	if ok:
		print "All tests pass"

	