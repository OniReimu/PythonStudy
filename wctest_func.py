#/usr/bin/python
#__author__ = 'User'

from optparse import OptionParser
import sys,os

def _option():
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
	options, args = parser.parse_args()
	return options,args

def _readData(options,args):
	global total_lines,total_words,total_chars
	total_lines,total_words,total_chars = 0, 0, 0  ## global variables
	if args:
		for fn in args:
			if os.path.isdir(fn):
				print  >> sys.stderr,"%s: %s: Is a directory" %(__file__,fn)     ## 2> /dev/null
				_printNull(options,fn)
				continue
			if not os.path.exists(fn):
				print  >> sys.stderr,"%s: %s: No such file or directory" %(__file__,fn)  ## 2> /dev/null
				continue
			with open(fn) as fd:
				data = fd.read()
				lines,words,chars = _getCount(data)
				_printResult(options,lines,words,chars,fn)
	else:
		fn = ''  ## There is no filename displayed when using standard input
		data = sys.stdin.read()
		lines,words,chars = _getCount(data)
		_printResult(options,lines,words,chars,fn)
#	return data,fn

def _getCount(data):
	global total_lines,total_words,total_chars
	chars = len(data)
	words = len(data.split())
	lines = data.count('\n')
	total_lines += lines
	total_words += words
	total_chars += chars
	return lines,words,chars

def _printResult(options,lines,words,chars,fn):
	if options.lines:
		print "%8s" %lines,
	if options.words:
		print "%8s" %words,
	if options.characters:
		print "%8s" %chars,
	print "%20s" %fn

def _printTotal(options,fn='total'):
	if options.lines:
		print "%8s" %total_lines,
	if options.words:
		print "%8s" %total_words,
	if options.characters:
		print "%8s" %total_chars,
	print  "%20s" %fn

def _printNull(options,fn):
	if options.lines:
		print "%8d" %0,
	if options.words:
		print "%8d" %0,
	if options.characters:
		print "%8d" %0,
	print  "%20s" %fn

def main():
	options,args = _option()
	## If all options are false, then turn them all into True
	if not (options.characters or options.words or options.lines):
		options.characters,options.words,options.lines = True,True,True
	_readData(options,args)
	if not options.nototal and not len(args) == 1:
		_printTotal(options)


if __name__ == '__main__':
	main()