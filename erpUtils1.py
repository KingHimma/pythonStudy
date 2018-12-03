#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Split
from datetime import datetime
import json
import requests
import cookielib

def exct(url, date = {}, cookies = ''):
	print url
	headers = {}
	return requests.post(url, data=json.dumps(date), cookies = cookies,headers= headers).content

def exctg(url, date = {}, cookies = ''):
	print url
	headers = {}
	return requests.get(url, data=json.dumps(date), cookies = cookies,headers= headers).content

def jsonPost(url, date = {}, cookies = ''):
	print url
	print date
	headers = {'Content-Type': 'application/json'}
	return requests.post(url, data=json.dumps(date), cookies = cookies,headers= headers).content

import time
import sched
import json
import requests

def getCookies(companyId):
	# tjCookies=
	# staff = json.loads(exctg('http://tj.erp.superboss.cc/tj/customer/queryStaff?api_name=tj_customer_queryStaff&companyId=8186&isVague=1',{},tjCookies)).get('data').get('list')[0]
	# print staff
	# ## 需要获取到第一个staff信息
	# url = 'http://tj.erp.superboss.cc/tj/customer/forward?companyId='+str(companyId)+'&staffId='+str(staff.get('id'));
	# cj = cookielib.CookieJar();
	# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
	# urllib2.install_opener(opener);
	# resp = urllib2.urlopen(url)
 #    print(resp)


companyIds = [8186,8265,5614,8222,8118,6635,7773,4185,8564,6945,2587,5127,4739,8527]
for y in companyIds:
	print companyIds
	pageNo = 1
	while True:
		print pageNo
		print getCookies(y)
		a = json.loads(exct('http://gray.erp.superboss.cc/trade/consign/detail?api_name=trade_consign_detail&isError=1&pageNo=%s&queryType=0&field=upload_time&order=desc&pageSize=100'%pageNo,{},getCookies(y))).get('data').get('list')
		needBreak = True
		sids = []
		for x in a:
			needBreak = False
			sids.append(x.get('sid'))
		if needBreak:
			break
		print exct('/trade/consign/upload/again?sids=%s'%','.join(sids),{},cookies)
		pageNo = pageNo + 1






