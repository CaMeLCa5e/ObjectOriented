#!/usr/bin/python

class Fish:
	"the things that are swimming in the bowl"
	fishCount = 0

	def __init__(self, FishName, FishColor):
		self.FishName = FishName
		self.FishColor = FishColor
		Fish.fishCount += 1

	def displayCount(self):
		print "Total fish in the bowl - %d" % Fish.fishCount

	def displayFish(self):
		print "Name : ", self.name, ", Color: ", self.FishColor

Fish1 = Fish("Bubbles", "red")
Fish2 = Fish("Nemo", "green")


print Fish1
print Fish2

if __name__ == '__main__':
	main()