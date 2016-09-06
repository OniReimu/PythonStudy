#/usr/bin/python

import sys
import os
from subprocess import Popen, PIPE

class Process(object):

	def __init__(self, name):
		self.name = name

	def _getPID(self):
		p = Popen(['pidof',self.name], stdout=PIPE)
		pid = p.stdout.read().strip()    ##delete \n
		return pid

	def _readPID(self):
		pid = self._getPID()
		self.mem = 0
		if pid:
			pidsplit = pid.split()
			for i in range(len(pidsplit)):
				with open(os.path.join('/proc/',pidsplit[i],'status')) as fd:
					for line in fd:
						if line.startswith('VmRSS'):
							self.mem = int(line.split()[1]) + self.mem
							break
			print "Mem information of %s has been read successfully" % self.name
		else:
			print "%s is terminated or not exists" % self.name

	def _totalMem(self):
		with open('/proc/meminfo') as fd:
			for line in fd:
				if line.startswith('MemTotal'):
					self.total = int(line.split()[1])
					break

	def _printResult(self):
		print "Total Memory: %.2f" % (self.total/1024.0)+' MB'
		print "Memory used of %s: %.2f" % (self.name,(self.mem/1024.0)) + ' MB,',
		print " Accounts for %.2f%%" % float((self.mem/1024.0)/(self.total/1024.0)*100)


def main():
	try:    ## Check if there is any args.
		name = sys.argv[1]
	except IndexError, e:
		print "Please enter the program you are targeting on"
		sys.exit()
	pm = Process(name=name)
	pm._readPID()
	pm._totalMem()
	pm._printResult()

if __name__ == '__main__':
	main()



