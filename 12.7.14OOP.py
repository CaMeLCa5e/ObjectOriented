#12.7.14OOP.py
class A(object):
	def whoami(self):
		return self.__class__.__name__

a = A()

print a.whoami()

