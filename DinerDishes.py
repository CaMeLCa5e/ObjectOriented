"""Drinks"""



class Dish(object):

	def __init__(self):
		self._clean = True

	def is_clean(self):
		return self._clean

	def state(self):
		return 'clean' if self.is_clean() else 'dirty'

	def __repr__(self):
		return 'An unspecified %s dish' %self.state()

	def _make_dirty(self):
		self._clean = False

	def wash(self):
		self._clean = True 

class Glass(Dish):
	
	def __init__(self, size):
		assert size > 0
		self._size = float(size) #attribute
		self.wash()

	def __repr__(self):
		if self._content == 0.0:
			return "An empty glass of size %s" %(self._size)
		else:
			return "A glass of size %s cl containing %s cl of water" %(
				self._size, self._content)
	
	def content(self):
		return self._content

	def beverage(self):
		return self.beverage

	def fill(self, beverage = 'water'):
		if not self.is_clean():
			raise ValueError('Please find new clean glass')
		self._clean = False
		self._content = self._size
		self._beverage = beverage
		self._content = self._size

	def empty(self):
		self._content = float(0.0)

	def is_empty(self):
		return self._content == 0.0
	
	def drink(self, amount):
		if amount <= 0.0:
			raise ValueError('Amount must be positive')
		elif amount > self._content:
			raise ValueError('not enough beverage in the glass')
		else:
			self._content -= float(amount)

	def is_clean(self):
		return self._clean

	def wash(self):
		self._content = float(0.0)
		self._beverage = None
		self._clean = True

class Spoon(Dish):

	def __repr__ (self):
		return 'a %s spoon' %self.state()

	def eat_with(self):
		self._make_dirty()



myGlass = Glass(10); myGlass
print myGlass

myGlass.fill(); myGlass
print myGlass

myGlass.empty(); myGlass
print myGlass

s = Spoon(); s
print s

print s.is_clean()

s.eat_with()

print s

print s.is_clean()


