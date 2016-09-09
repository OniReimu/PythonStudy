#!/usr/bin/python

from subprocess import PIPE,Popen
import shlex
import re

def readCoreNum():
    number = 0
    p = Popen(shlex.split("cat /proc/cpuinfo"),stdout=PIPE,stderr=PIPE)
    data = p.stdout.read().split('\n')
    data = [i for i in data if i]
    for i in data:
        processor = re.match("^processor",i)
        if processor:
            number += 1
    return data,number

def readCoreVersion(data):
    CPUlist = []
    for i in data:
        if i.startswith("model name"):
            CPUlist.append(i.split(':')[1].strip())
    return CPUlist
            
def main():
    data,number = readCoreNum()
    CPUlist = readCoreVersion(data)
    return number,CPUlist    

if __name__ == '__main__':
    print main()
