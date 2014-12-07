class Song(object):
	def __init__(self, title, artist):
		self.title = title
		self.artist = artist
	def get_title(self):
		return self.title
	def get_artist(self):
		return self.artist

leave = Song('Leave', 'Glen Hansard')
print leave
print leave.title 
leave.title = 'Please Leave'
print leave.title
# print leave.__title

class Adder(object):
	def __init__(self, extra):
		self.extra = extra
	def __call__(self, base):
		return self.extra + base

add2 = Adder(2)
print add2(3)
print add2(7)
add5 = Adder(5)
print add5(5)


# class Lister(object):
# 	def __init__ (self, *args):
#        self.items = tuple(args)
# 	def __iter__(self):
# 		return (i for i in self.items)

class Lister(object):
	def __init__(self, *args):
		self.items = tuple(args)
	def __iter__(self):
		for i in self.items:
			yield i 
l = Lister('a', 'b', 'c')
for letter in l:
	print letter
