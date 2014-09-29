# coding: utf-8
#series program
""" runs the Fibonacci series  """
def Fibonacci(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 1
	else:
		return Fibonacci(n - 1) +  Fibonacci(n - 2)
""" runs the Lucas series """
def Lucas(n):
	if n <= 0:
		return 0
	elif n == 1:
		return 2
	elif n == 2:
		return 1
	else:
		return Lucas(n - 1) + Lucas(n - 2)
""" runs the nth number series """
def sum_series(n, n0 = 0, n1 = 1):
	if n < 0:
		return 0
	elif n == 0:
		return n0
	elif n == 1:
		return n1
	else:
		return sum_series(n - 1, n0, n1) + sum_series(n - 2, n0, n1)
if __name__ =="__main__":
	Fib = [0,1,1,2,3,5,8,13]
	Luc	= [0,2,1,3,4,7,11,18]
	for n, (exf, exl) in enumerate(zip(Fib,Luc)):
		#print exf, exl 
		assert Fibonacci(n) == exf 
		assert Lucas(n) == exl
		print sum_series(n)
		assert Fibonacci(n) == sum_series(n)
	print "All tests pass"


