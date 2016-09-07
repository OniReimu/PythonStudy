#/usr/bin/python
# Note that the main step to transfer from functional type to class type is to add 'self.' in front of each variable
# that needs to be transferred into other functions.

from optparse import OptionParser
import sys,os

class Process(object):

	def _option(self):
		parser = OptionParser()
		parser.add_option("-c","--chars",
						  dest="characters",
						  action="store_true",
						  default=False,
						  help="only count characters",)

		parser.add_option("-w","--words",
						  dest="words",
						  action="store_true",
						  default=False,
						  help="only count words",)

		parser.add_option("-l","--lines",
						  dest="lines",
						  action="store_true",
						  default=False,
						  help="only count lines",)

		parser.add_option("-n","--no-total",
						  dest="nototal",
						  action="store_true",
						  default=False,
						  help="not show total",)
		self.options, self.args = parser.parse_args()
		## If all options are false, then turn them all into True
		if not (self.options.characters or self.options.words or self.options.lines):
			self.options.characters,self.options.words,self.options.lines = True,True,True

	def _readData(self):
		global total_lines,total_words,total_chars
		total_lines,total_words,total_chars = 0, 0, 0  ## global variables
		if self.args:
			for self.fn in self.args:
				if os.path.isdir(self.fn):
					print  >> sys.stderr,"%s: %s: Is a directory" %(__file__,self.fn)     ## 2> /dev/null
					self._printNull()
					continue
				if not os.path.exists(self.fn):
					print  >> sys.stderr,"%s: %s: No such file or directory" %(__file__,self.fn)  ## 2> /dev/null
					continue
				with open(self.fn) as fd:
					self.data = fd.read()
					self._getCount()
					self._printResult()
		else:
			self.fn = ''  ## There is no filename displayed when using standard input
			self.data = sys.stdin.read()
			self._getCount()
			self._printResult()

	def _getCount(self):
		global total_lines,total_words,total_chars
		self.chars = len(self.data)
		self.words = len(self.data.split())
		self.lines = self.data.count('\n')
		total_lines += self.lines
		total_words += self.words
		total_chars += self.chars

	def _printResult(self):
		if self.options.lines:
			print "%8s" %self.lines,
		if self.options.words:
			print "%8s" %self.words,
		if self.options.characters:
			print "%8s" %self.chars,
		print "%20s" %self.fn

	def _printTotal(self):
		if self.options.lines:
			print "%8s" %total_lines,
		if self.options.words:
			print "%8s" %total_words,
		if self.options.characters:
			print "%8s" %total_chars,
		print  "%20s" %"total"

	def _printNull(self):
		if self.options.lines:
			print "%8d" %0,
		if self.options.words:
			print "%8d" %0,
		if self.options.characters:
			print "%8d" %0,
		print "%20s" %self.fn

def main():
	pm = Process()
	pm._option()
	pm._readData()
	## Justify if to show total
	if not pm.options.nototal and not len(pm.args) == 1:
		pm._printTotal()


if __name__ == '__main__':
	main()