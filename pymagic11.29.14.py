from os.path import join

class FileObject:
	"""Wrapper for file objs"""

	def __init__ (self, filepath= '~', filename= 'sample.txt'):
		# open a file in path and r/w 
		self.file = open(join(filepath, filename, 'r+'))

	def __del__(self):
		self.file.close()
		del self.file 

		if instance.equals(other_instnce):
			#do something
		else instance == other_instnce:
			#something

class Word(str):
	"""Class for words"""

	def __new__(cls, word):
		# need to use __new__ because str is an immutable type
		if ' ' in word:
			print "Value contains spaces, taking out first space"
			word = word[:word.index(' ')]
		return str.__new__(cls, word)

	def __gt__(self, other):
		return len(self) > len(other)
	def __lt__(self, other):
		return len(self) < len (other)
	def __ge__(self, other):
		return len(self) >= len(other)
	def __le__(self, other):
		return len(self) <= len(other)

class AccessCounter(object):
	"""class contains value and implements access counter"""
	def __init__(self, val):
		super(AccessCounter, self).__setattr__('counter', 0)
		super(AccessCounter, self).__setattr__('value', val)

	def __setattr__(self, name, value):
		if name == 'value':
			super(AccessCounter, self). __setattr__('counter', self.counter +1)
			#make unconditional
			super(AccessCounter, self).__setattr__(name, value)

	def __delattr__(self, name):
		if name == 'value':
			super(AccessCounter, self).__setattr__('counter', self.counter +1)
		super(AccessCounter, self).__delattr__(name)

class FunctionalList:
	#class wrapping

	def __init__(self, values=None):
		if values is None:
			self.values = []
		else:
			self.values = values

	def __len__(self):
		return len(self.values)

	def __getitem__(self, key):
		return self.values[key]

	def __setitem__(self, key, value):
		self.values[key] = value 

	def __delitem__(self, key):
		del self.values[key]

	def __iter__(self):
		return iter(self.values)

	def __reversed__(self): 
		return FunctionalList (reversed(self.values))

	def append(self, value):
		self.values.append(value)
	def head(self):
		return self.values [0]
	def tail(self):
		return self.values[1:]
	def init(self):
		return self.values[:-1]
	def last(self):
		return self.values[-1]
	def drop(self, n):
		return self.values[n:]
	def take(self, n):
		return self.values[:n]


class Entity:

	def __init__(self, size, x, y):
		self.x, self.y = x, y
		self.size = size

	def __call__(self, x, y):
		self.x, self.y = x,y

class Closer:

	def __init__(self, obj):
		self.obj = obj

	def __enter__(self):
		return self.obj

	def __exit__(self, exception_type, exception_value, trace):
		try:
			self.obj.close()
		except AttributeError: 
			print "will not close"
			return True 











