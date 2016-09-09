#!/usr/bin/python

from subprocess import Popen,PIPE

def getVersion():
    p = Popen(['cat','/etc/issue'],stdout=PIPE,stderr=PIPE)
    stdout,stderr = p.communicate()
    data = stdout.split('\n')[0]
    return data

def main():
    data = getVersion()
    return data

if __name__ == '__main__':
    print main()
