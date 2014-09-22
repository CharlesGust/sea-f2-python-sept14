def fibonacci(n):
	"""Returns the Nth Fibonacci number, where f(n) = f(n - 1) + f(n - 2), f(0) = f(1) = 1"""
	if n < 0: 
		return None
	elif n == 0: 
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
	"""Returns the Nth Lucas number, where l(n) = l(n - 1) + l(n - 2), l(0) = 2, l(1) = 1"""
	if n < 0:
		return None
	elif n == 0:
		return 2
	elif n == 1:
		return 1
	else:
		return lucas(n - 1) + lucas(n - 2)

def sum_series(n, n1 = 0, n2 = 1):
	"""Returns the Nth number in the series, where s(n) = s(n - 1) + s(n - 2), s(0) = n1, s(1) = n2"""
	if n < 0:
		return None
	elif n == 0:
		return n1
	elif n == 1:
		return n2
	else:
		return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2)

if __name__ == '__main__':

	fib_test = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

	luc_test = [2, 1, 3, 4, 7, 11, 18, 29, 47, 76, 123]

	s_test1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
	"""n1 = 0, n2 = 1"""

	s_test2 = [2, 5, 7, 12, 19, 31, 50, 81, 131, 212, 343]
	"""n1 = 2, n2 = 5"""

	for i in range(11):
		assert fibonacci(i) == fib_test[i]
		assert lucas(i) == luc_test[i]
		assert sum_series(i) == s_test1[i]
		assert sum_series(i, 2, 5) == s_test2[i]

	print "All Tests Pass"
