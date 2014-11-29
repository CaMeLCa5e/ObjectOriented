

class className:
	def createName(self, name):
		self.name = name
	def displayName(self):
		return self.name
	def saying (self):
		print "hello %s" % self.name

first = className()
second = className()
first.createName('Jack')
second.createName('Pumba')

print first.displayName()
print second.displayName()
print first.saying()
print second.saying()