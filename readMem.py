#!/usr/bin/python


def _totalMem():
    total = 0
    with open('/proc/meminfo') as fd:
        for line in fd:
            if line.startswith('MemTotal'):
                total = int(line.split()[1])
                if total < 1024**3:
                    total = str(total/1024.0)+' MB'
                elif total > 1024**3:
                    total = str(total/1024.0/1024.0)+' GB'
                break

    return total

if __name__ == '__main__':
    print _totalMem()
