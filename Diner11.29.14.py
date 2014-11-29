class Glass(object):
	def __init__(self, size):
		assert size > 0
		self._size = float(size) 
		self._content = float(0.0)
	def __repr__(self):
		if self._content == 0.0:
			return "An empty glass of size %s" %(self._size)
		else:
			return "A glass of size %s cl containing %s cl of water" %(
				self._size, self._content)

	def fill(self):
		self._content = self._size
	def empty (self):
		self._content = float(0.0)


myGlass = Glass(10); myGlass
print myGlass

class Spoon(object):
	def __init__(self, size):
		assert size > 0
		self._size = float(size)
		self._content = float(0.0)
	def __repr__(self):
		return "No spoon.  HA!"

		else:
			return "I have a spoon"

mySpoon = Spoon(6); mySpoon
print mySpoon



