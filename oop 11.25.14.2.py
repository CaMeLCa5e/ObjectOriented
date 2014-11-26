#oop 11.25.14.2.py
 
class Numchange:

	def __init__(self):
		self.__number = 0

	def addfive(self,num):
		self.__number = num
		return self.__number + 5

	def multiply(self, added):
		self.__added = added
		return self.__added * 2.452 

maths = Numchange()

def main():
	
	num = float(input('Please enter a number. \n'))

	added = maths.addfive(added)

	multip = maths.multiply(added)

	print('The manipulated value is ', multip)

main()
