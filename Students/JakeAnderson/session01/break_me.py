

""" syntax error """ 
def fun(3, 44, 23):
	print 3, 44, 23

 """ name error  """
def fun(test = 4 + spam * 3):
	print test

 """ type error """
def fun(this = 'that' + 5):
	print this 

""" attribute error """
def fun(something = 5 + '6'.tolower ):
	print something
