#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##  工具做去重 并且给出所有结果
dmap = {}
with open('/Users/gongdaoyan/Documents/sublime Text/python/countFile', 'r') as f:
	str = f.readlines()
	for x in str:
		key = x.replace('\n','')
		count = dmap.get(key, 0)
		count = count + 1
   		dmap[key] = count

print dmap.__len__()
# print dmap

# file = open('/Users/gongdaoyan/Documents/sublime Text/python/result','w')
count = 0
print dmap
for x in dmap:
	# if dmap.get(x) == 1:
	print(x)
		# count = count + 1
		# print count
	# file.write(x)
	# file.write(';')


