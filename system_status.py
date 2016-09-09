#!/usr/bin/python

from pymodules import readDmidecode, readIPinfo, readVersion, readCPU, readMem
from subprocess import PIPE,Popen

def hostnameDisplay():
    p = Popen(['hostname'], stdout=PIPE, stderr=PIPE)
    return p.stdout.read()

def main():
    print '\n'+'#'*90
    print "\n%-20s: %s" % ('Hostname',hostnameDisplay()),
    print "%-20s: %s" % (readDmidecode.dmiDic().keys()[2],readDmidecode.dmiDic().values()[2])
    print "%-20s: %s" % (readDmidecode.dmiDic().keys()[1],readDmidecode.dmiDic().values()[1])
    print "%-20s: %s" % (readDmidecode.dmiDic().keys()[0],readDmidecode.dmiDic().values()[0])
    print "Network:\n",
    for i in xrange(len(readIPinfo.main())):
        print "\t\t%s:" % readIPinfo.main().keys()[i]
        print "\t\t\tIp address: %s" % readIPinfo.main().values()[i][0]
        print "\t\t\tMac address: %s" % readIPinfo.main().values()[i][1]
    print "OS Version: %-20s" % readVersion.main()
    print "Number of Core: %s" % readCPU.main()[0]
    print "Core Version:"
    for i in xrange(len(readCPU.main()[1])):
        print "\tProcessor %d: %s" %((i+1),readCPU.main()[1][i])
    
    print "Memory Informaiton: %s" %readMem._totalMem()
    print '\n'+'#'*90+'\n'    

if __name__ == '__main__':
    main()
