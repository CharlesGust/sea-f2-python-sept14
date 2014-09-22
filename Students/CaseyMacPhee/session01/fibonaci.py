def fib(ceiling):
	if ceiling is 0:
		return 1
	else:
		print ceiling
		return ceiling * fib(ceiling -1)

x = fib(200)
print x
