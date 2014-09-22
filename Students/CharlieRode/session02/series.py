def fibonacci(n):
	"""Returns the Nth Fibonacci number, where f(n) = f(n - 1) + f(n - 2), f(1) = f(2) = 1"""
	if n <= 0: 
		return None
	elif n <= 2: 
		return 1
	else:
		return fibonacci(n - 1) + fibonacci(n - 2)

def lucas(n):
	"""Returns the Nth Lucas number, where l(n) = l(n - 1) + l(n - 2), l(1) = 2, l(2) = 1"""
	if n <= 0:
		return None
	elif n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return lucas(n - 1) + lucas(n - 2)

def sum_series(n, n1 = 0, n2 = 1):
	"""Returns the Nth number in the series, where s(n) = s(n - 1) + s(n - 2), s(1) = n1, s(2) = n2"""
	if n <= 0:
		return None
	elif n == 1:
		return n1
	elif n == 2:
		return n2
	else:
		return sum_series(n - 1, n1, n2) + sum_series(n - 2, n1, n2)

