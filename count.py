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

print dmap

for x in dmap:
	count = dmap.get(x, 0)
	if count > 10:
		print(x, count)
	

