#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import Split
from datetime import datetime
import json
import requests

## 登录
login = requests.post('http://erp.superboss.cc/account/login',{'companyName':'小五测试','password':'55A86C51427E48F486272A465CE15D73','salt':'1540270047131','userName':'admin'})
cookies =  login.cookies

## 执行请求
def exct(url, date = {}, cookies = ''):
	return json.loads(requests.post('http://erp.superboss.cc/%s'%url, date, cookies = cookies ).content)


for x in range(100):
	url = '/trade/search'
	data = {
			'api_name':'trade_search',
			'queryId':'26',
			'pageNo': x,
			'pageSize':'5'
			}
	print exct(url, data, cookies)



	