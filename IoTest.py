#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Split

def split(count = 1):
	for x in range(count):
		print '==================================================================================================================================================='


file = open('/Users/gongdaoyan/Documents/sublime Text/python/test.py','r')
split(3)
# with open('/Users/gongdaoyan/Documents/sublime Text/python/test.py', 'r') as f:
#     print(f.read())
file.close()
split(3)
file = open('/Users/gongdaoyan/Documents/sublime Text/python/io','w')
file.write('## test io writelines')
file.close()
file = open('/Users/gongdaoyan/Documents/sublime Text/python/io','r')
print file.read()
file.close()

Split.split()

import os
print os.name
