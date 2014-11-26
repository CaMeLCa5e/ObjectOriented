

def main():
	try:
		# get a new number
		num = float(input('please enter a number. \n'))
		# store the result
		addednum = addfive(num)
		# store the result of the value
		multipliednum = multiply(addednum)
		# send value to Procedure 4
		
	except ValueError:
		print('You must enter a valid number. \n')
		# reset the number to clear non-numeral types
		num = 0 
		# call main again 
		main()

# Procedure 2
def addfive(num):
	return num +5

# Procedure 3
def multiply(addednum):
	return addednum * 2.452 

# Procedure 4
def display(multi):
	#display the final value 
	print ('the final value is ', multi)

#call Procedure 1
main()