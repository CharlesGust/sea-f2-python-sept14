def misnomer(strng):
	"""Run misnomer() to demonstrate the NameError exception"""
	result = string
	return result

def unlike_the_other(num):
	"""Run unlike_the_other() to demonstrate the TypeError exception"""
	return len(num)

#def what(arr):
#    """Uncomment what() to demonstrate the SyntaxError exception"""
#	 result = 0
#	 for x in arr:
#	     result += x
#	 retrun result




class Animal(object):
    """A class to help demonstrate the AttributeError exception"""
    def __init__(self, name, has_nipples):
    	self.name = name
    	self.has_nipples = has_nipples

class Mamal(Animal):
	def __init__(self, name):
	    self.name = name
	    self.has_nipples = True

	def milk(self):
		"""Run milk() on snake to demonstrate the AttributeError exception"""
		print "You milked the %s!" % self.name



cow = Mamal("Cow")
"""Cows have nipples. You can milk Cows."""

cat = Mamal("Cat")
"""Cats have nipples. You can milk Cats."""

snake = Animal("Snake", False)
"""Snakes do not have nipples. You cannot milk Snakes."""

