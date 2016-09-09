#!/usr/bin/python

from subprocess import Popen, PIPE

def getDmi():
    p = Popen(['dmidecode'], stdout=PIPE)
    data = p.stdout.read()
    return data

def parseDmi(data):
    lines = []
    line_in = False
    dmi_list = [i for i in data.split('\n') if i]
    for line in dmi_list:
        if line.startswith('System Information'):
            line_in = True
            continue
        if line_in:
            if not line[0].strip():
                lines.append(line)
            else:
                break
    return lines

def dmiDic():
    dmi_dic = {}
    data = getDmi()
    lines = parseDmi(data)
    dic = dict([i.strip().split(':') for i in lines])
    dmi_dic['Manufacturer'] = dic['Manufacturer'].strip()
    dmi_dic['Product Name'] = dic['Product Name'].strip()
    dmi_dic['Serial Number'] = dic['Serial Number'].strip()
    return dmi_dic

if __name__ == '__main__':
    print dmiDic()
