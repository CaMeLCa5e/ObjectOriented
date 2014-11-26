#recursion 11.25.14.py

num = 0

def main():
	counter(num)

def counter(num):
	print(num)
	num += 1
	counter(num)

main()

