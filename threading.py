import threading
from random import randint
from time import sleep

def printNumber(number):
	#sleeps random # 1-10
	sleep(randint(1,10))
	print str(number)

thread_list = []

for i in range(1,10):
	#instantiates the thread
	t = threading.Thread(target=printNumber, args=(i,))
	#keeps thread in a list 
	thread_list.append(t)

#Start thread
for thread in thread_list:
	thread.start()

for thread in thread_list:
	thread.join()

print "Done"









