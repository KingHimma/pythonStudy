#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 打印日志查询工具

import Split
from datetime import datetime
import json
import requests

import sys
# 解决编码问题
reload(sys)
sys.setdefaultencoding('utf-8')


## 需要在日志中搜索的单号信息
outSids = [7]
# for sid in sids:
# 	date = json.loads(exct( "/trade/multipacks/outSid/query?sid=%s"%sid,"",cookies))
# 	for x in date["data"]:
# 		outSids.append(x["outSid"])

printSid=[]
file = open('/Users/gongdaoyan/Documents/sublime Text/python/result','w')


count = 0
allSid = []
with open('/Users/gongdaoyan/Documents/sublime Text/python/logFile', 'r') as f:
	print '1'
	str = f.readlines()
	for s in str:
		count = count +1
		hasSid = []
		for x in outSids:
			xstr = "%s"%x
			if xstr in s :
				if x not in allSid:
					allSid.append(x)
				hasSid.append(x)
		if hasSid.__len__() > 0:
			print(','.join('%s' % id for id in hasSid), '--------------',count)
			file.writelines(','.join('%s' % id for id in hasSid))
			file.write('-----')
			file.write( s)

print ','.join('%s' % id for id in hasSid)
print allSid.__len__()

print '-----------'
for a in outSids:
	if a not in allSid:
		print a




	# for x in str:
	# 	key = x.replace('\n','')
	# 	count = dmap.get(key, 0)
	# 	count = count + 1
 #   		dmap[key] = count


