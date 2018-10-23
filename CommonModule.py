#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import Split
from datetime import datetime
import json
import requests
now = datetime.now()

print now
print now.now().timetuple()


## 登录
p = requests.post('http://erp.superboss.cc/account/login',{'companyName':'小五测试','password':'55A86C51427E48F486272A465CE15D731','salt':'1540270047131','userName':'admin'})
cookies =  p.cookies

date = {
	'api_name':'trade_search',
	'queryId':'26',
	'pageNo':'1',
	'pageSize':'5'
}
t = requests.post('http://erp.superboss.cc/trade/search', date, cookies = cookies )
tradeModels = json.loads(t.content) 
print tradeModels.get('data').get('list')[1]

## Json 转换
d = {"a":1,"b":2}

print(d)
f = json.dumps(d)
print(type(f))
print(f)
e = json.loads(f)
print(type(e))
print(e)





