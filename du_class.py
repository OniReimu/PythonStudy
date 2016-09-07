#/usr/bin/python
# Note that the main step to transfer from functional type to class type is to add 'self.' in front of each variable
# that needs to be transferred into other functions.

from optparse import OptionParser
import sys,os

global count
count = 1
class Process(object):

	def __init__(self):
		self.dirlist = []  ## subdirs list
		self.list = []   ## files list
		self.size = []    ## str type
		self.sizecal = []  ## int type
		self.total = 0     ## calculate total

	def _option(self):
		parser = OptionParser()
		parser.add_option("-H","--humanreadable",
						  dest="humanreadable",
						  action="store_true",
						  default=False,
						  help="human readable",)
		self.options, self.args = parser.parse_args()

	def _tracedownDir(self,name=''):
		global count
		if count == 1:
			name = self.fn
			count += 1
		isdir, isfile, join = os.path.isdir, os.path.isfile, os.path.join
		Isdir = os.listdir(name)
		dirs = [i for i in Isdir if isdir(join(name,i))]
		files = [i for i in Isdir if isfile(join(name,i))]
		if dirs:
			for d in dirs:
#				print join(name,d)
				self.dirlist.append(join(name,d))
				self._tracedownDir(join(name,d))
		if files:
			for f in files:
#				print join(name,f)
				self.list.append(join(name,f))
		self.dir = name

	def _getSize(self):
		for path in self.list:
			i = 1
			tempsize = os.path.getsize(path)
			while tempsize > 4096*i:
				i += 1
			if not self.options.humanreadable:
				self.size.append(str(4096*i))
				self.sizecal.append(4096*i)
			else:
				self.sizecal.append(4096*i)
				if tempsize < 1024**2:
					self.size.append(str(4096*i/1024.0) + 'K')
				elif tempsize >= 1024**2 and tempsize < 1024**3:
					self.size.append(str(40964*i/1024.0/1024.0) + 'M')
				elif tempsize >= 1024**3 and tempsize < 1024**4:
					self.size.append(str(4096*i/1024.0/1024.0/1024.0) + 'G')
				elif tempsize >= 1024**4 and tempsize < 1024**5:
					self.size.append(str(4096*i/1024.0/1024.0/1024.0/1024.0) + 'T')
		self.total = sum(self.sizecal)
		#self.total = reduce(lambda x, y: x+y, self.sizecal)

	def _printResult(self):
		if self.options.humanreadable:
			if self.total < 1024**2:
				self.total = (str(self.total/1024.0) + 'K')
			elif self.total >= 1024**2 and self.total < 1024**3:
				self.total = (str(self.total/1024.0/1024.0) + 'M')
			elif self.total >= 1024**3 and self.total < 1024**4:
				self.total = (str(self.total/1024.0/1024.0/1024.0) + 'G')
			elif self.total >= 1024**4 and self.total < 1024**5:
				self.total = (str(self.total/1024.0/1024.0/1024.0/1024.0) + 'T')
		filedic = dict(zip(self.list,self.size))
		filedic.update({self.dir:self.total})
		for k,v in filedic.items():
			print "%s : %s" %(v,k)

	def _tracedownSubdir(self):
		lists = self.dirlist
		for d in lists:
			self.dirlist = []   ## clear the subdirs list
			self.list = []   ## clear the files list
			self.size = []
			self._tracedownDir(d)
			self._getSizeSubdir()
			self._printResultSubdir()

	def _getSizeSubdir(self):
		for path in self.list:
			i = 1
			tempsize = os.path.getsize(path)
			while tempsize > 4096*i:
				i += 1
			self.size.append(4096*i)
		if not self.size:
			self.size = [4096]    ## Still occupied 4K for empty dir
		self.total = sum(self.size)

	def _printResultSubdir(self):
		if self.options.humanreadable:
			if self.total < 1024**2:
				self.total = (str(self.total/1024.0) + 'K')
			elif self.total >= 1024**2 and self.total < 1024**3:
				self.total = (str(self.total/1024.0/1024.0) + 'M')
			elif self.total >= 1024**3 and self.total < 1024**4:
				self.total = (str(self.total/1024.0/1024.0/1024.0) + 'G')
			elif self.total >= 1024**4 and self.total < 1024**5:
				self.total = (str(self.total/1024.0/1024.0/1024.0/1024.0) + 'T')
		filedic = {self.dir:self.total}
		for k,v in filedic.items():
			print "%s : %s" %(v,k)

	def _getSizeFile(self):
		i = 1
		self.total = os.path.getsize(self.fn)
		self.dir = self.fn
		while self.total > 4096*i:
			i += 1
		if not self.options.humanreadable:
			self.total = str(4096*i)
		else:
			self.total = 4096*i
		if self.options.humanreadable:
			if self.total < 1024**2:
				self.total = (str(self.total/1024.0) + 'K')
			elif self.total >= 1024**2 and self.total < 1024**3:
				self.total = (str(self.total/1024.0/1024.0) + 'M')
			elif self.total >= 1024**3 and self.total < 1024**4:
				self.total = (str(self.total/1024.0/1024.0/1024.0) + 'G')
			elif self.total >= 1024**4 and self.total < 1024**5:
				self.total = (str(self.total/1024.0/1024.0/1024.0/1024.0) + 'T')
		filedic = {self.dir:self.total}
		for k,v in filedic.items():
			print "%s : %s" %(v,k)

	def _control(self):
		if self.args:
			for self.fn in self.args:
				if not os.path.exists(self.fn):
					print  >> sys.stderr,"%s: cannot access %s: No such file or directory" %(__file__,self.fn)  ## 2> /dev/null
					continue
				if os.path.isfile(self.fn):
					self._getSizeFile()
				elif os.path.isdir(self.fn):
					self._tracedownDir()
					self._getSize()
					self._printResult()
					self._tracedownSubdir()
		else:
			self.fn = os.getcwd()
			self._tracedownDir()
			self._getSize()
			self._printResult()
			self._tracedownSubdir()

def main():
	pm = Process()
	pm._option()
	pm._control()

if __name__ == '__main__':
	main()