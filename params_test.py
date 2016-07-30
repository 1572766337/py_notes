#coding:utf8

'''
一直很好奇sqlmap的参数功能怎么实现的
以下代码，来入个门
'''

import sys, getopt

opts, args = getopt.getopt(sys.argv[1:], "u:f:")

def usage():
    print "Usage:"

for op, value in opts:
    if op == "-u":
        url = value
        print url
    elif op == "-f":
        print value
    else:
        usage()
        sys.exit()
