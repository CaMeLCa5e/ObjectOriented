#!/usr/bin/env python 

import subprocess
import threading

class Pinger(object):
	status = {'alive': [], 'dead': []} #populated while program is running
	hosts = [] #list of hosts/ips in input queue

	#number of ping processes at a time. 
	thread_count = 4

	#lock object to keep track of the threads in loops.  
	lock = threading.Lock()

	def ping(self, ip):
		# use system ping command with a count of 1 and wait of 1. 
		ret = subprocess.call(['ping', '-c', '1', '-w', '1', ip], 
							stdout=open('/dev/null', 'w'), stderr=open('/dev/null', 'w'))
		return ret == 0 # Return True if ping command succeeds

	def pop_queue(self):
		ip = None

		self.lock.acquire() #Grab or wait+Grab the lock 

		if self.hosts:
			ip = self.hosts.pop()

		self.lock.release() #release lock so another thread can run

		return ip 

	def dequeue(self):
		while True:
			ip = self.pop_queue()

			if not ip:
				return None

			result = 'alive' if self.ping(ip) else 'dead'
			self.status[result].append(ip)

	def start(self):
		threads = []

		for i in range (self.thread_count):
			#create self.thread_count number of threads that remove each ip from the list.  
			t = threading.Thread(target=self.dequeue)
			t.start()
			threads.append(t)

		[ t.join for t in threads ]

		return self.status

if name == '__main__':
	ping = Pinger()
	ping.thread_count = 8
	ping.hosts = [
		'10.0.0.1', '10.0.0.2', '10.0.0.3', '10.0.0.4', '10.0.0.0', '10.0.0.255', '10.0.0.100',
		'google.com', 'github.com', 'nonexisting', '127.0.1.2', '*not able to ping!*', '8.8.8.8'
		]

	print ping.start

















