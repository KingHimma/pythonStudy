#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import Split
from datetime import datetime
import json
import requests

## 登录
# login = requests.post('http://erp.superboss.cc/account/login',{'companyName':'小五测试','password':'55A86C51427E48F486272A465CE15D73111','salt':'1540270047131','userName':'admin'})
# cookies =  login.cookies

## 执行请求
def exct(url, date = {}, cookies = ''):
	print url
	headers = {}
	return requests.post('http://gray.erp.superboss.cc/%s'%url, data=json.dumps(date), cookies = cookies,headers= headers).content

def jsonPost(url, date = {}, cookies = ''):
	print url
	print date
	headers = {'Content-Type': 'application/json'}
	return requests.post('http://local.erp.superboss.cc/%s'%url, data=json.dumps(date), cookies = cookies,headers= headers).content


# def jsonPost(url, date = {}, cookies = ''):
# response = requests.post(url='url', headers=headers, data=json.dumps(data))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import sched
import json
import requests

# schedule = sched.scheduler ( time.time, time.sleep )

# def func():
# 	print 'aaa'
# 	data = {'msgtype':'text','text':{'content':'testContent'}}
# 	header = {"Content-Type": "application/json", "Charset": "UTF-8"}
# 	res=requests.post('https://oapi.dingtalk.com/robot/send?access_token=a22af7c9f944573bf1d0958c66271684d1f3243982b7729f8104df835ea7b506',data=data,headers=header)

# print(time.time())
# func()

# schedule.enter(1,0,func,())
# schedule.run()

# for x in range(100):
# 	url = '/trade/search'
# 	data = {
# 			'api_name':'trade_search',
# 			'queryId':'26',
# 			'pageNo': x,
# 			'pageSize':'5'
# 			}
# 	print exct(url, data, cookies)

# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10290','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10293','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10295','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10297','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10298','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10299','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10300','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10559','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10560','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10561','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10562','',cookies)
# print exct( 'trade/sync?companyId=7591&startTime=2018-11-11 00:00:00&syncType=2&userId=10563','',cookies)



# cookies = ""

# sids = {258986432704431452,238398630297566685,244081901891586503,238596102552090474,244397742977957018,259492545300000757,244179821209477414,238827815513393396,259684898850364644,244883823124586503,259945601107534759,244464205492586503,259990369315431452,239050023573121388,244767150682477414,260115618858534759,244503948173586503,238860420812090474,245046894214586503,245001678676199103,245313679311199103,239505831654288396,238949188061288396,260420640623344527,244811500909199103,260726946727205948,260857474923862460,239688647225121388,261179043333979439,239345445191774170,245269806822214905,239294340625774170,260768640122318460,239330180900574979,239354180887574979,261449923133998267,260852257270782053,261436419958862460,261011136126773046,261225185051773046,261546179205998267,244557709096586503,239595493987346088,261264641424782053,239660229554958198,239606597415346088,240029319463958198,240051303323958198,261094240454999938,245797199862973407,239851494069958198,245819983392450425,261213568667205948,260280419869031162,240250182650480883,239904390195856787,239834629020916478,245667502679058915,261284160877999959,239956518552856787,245251308668450425,239998374659856787,239997318308856787,261666402957581657,245734894184973407,261549313331782053,245494924741452904,245969487551452904,261711393919318460,245830350313037625,261620864893474733,261592544622964765,262148835760031162,239926756663254070,261694369753964765,245666380125716909,261959585482476455,261841250708424042,240078181555480883,245600396961046822,245716908733957018,261985217711815633,261413664172782053,262108866691663830,246228175600262108,261786624227663830,245811181602141009,245891789108037625,239020132723288396,262292897637000757,240347877725393396,245881357569716909,260189281550344527,240679623404254070,262174336718287363,262452482626287363,262769251086287363,262209728142287363,246541167416058915,246080973319590312,246200717951651019,262967906781477829,261227427566979439,262939713901575254,263054242284824643,262796704284824643,263356931982477829,263094018699571452,240823140133937680,241159911547149270,263468419640581657,262906336428803862,241132486677937680,246432557254590312,246395117334104021,246932207809104021,263483779159815633,263006400330803862,263259266674307462,246938159866262108,263594243748575254,263063360500307462,263723459636000757,247035215882681502,246861998940681502,246598604006681502,247063727616651019,263823747224142254,263207168198142254,263864611226431452,241101796517958198,246726861313916706,247216015830916706,246753004219916706,241723303180833376,263718081935979439,241582918234566685,247106830403284316,246820429376284316,264043489940998267,241567972384833376,241550916284853494,241876390816853494,242076615352853494,247337742571046822,264477218869014365,247227853273141009,241991878233393396,264498241178474733,242089062997393396,241826436141600699,247257645278717112,247308973834586503,247794671655717112,265013283602376251,242194982578149270,242280038947149270,264926914404376251,264694528102014365,265274211490424042,247956751497214905,264765888276917765,264785952651917765,264875968069581657,265179169213999938,242404964594149270,242529797439149270,265160960379360855,265402305699999938,242946663551221493,242786567442221493,242773478951322790,248125166357141009,242714950003600699,265564034923571452,265925667935964765,265182304046964751,265660546335999959,265644514048964751,266006531456964751,242638948593322790,247998765974287208,265706434446360855,242782949630322790,265726338682364644,266053443619364644,266133635073431452,243002790694322790,248573871546477414,248229421737127408,248463919349141009,248588494140287208,243541191521916478,266540322132476455,248560652660127408,243635077613407569,243525348013407569}
# for sid in sids:
# 	date = json.loads(exct( "/trade/multipacks/outSid/query?sid=%s"%sid,"",cookies))
# 	for x in date["data"]:
# 		print x["outSid"]

# print
# print exct( "/trade/multipacks/outSid/query?sid=1962849293718528","",cookies)
# print exct( "/trade/multipacks/outSid/query?sid=1962756399174656","",cookies)
# print exct( "/trade/multipacks/outSid/query?sid=1962722378273280","",cookies)
# print exct( "/trade/multipacks/outSid/query?sid=1962657600868864","",cookies)
# print exct( "/trade/multipacks/outSid/query?sid=1962569456914944","",cookies)
# print exct( "/trade/multipacks/outSid/query?sid=1960572581876736","",cookies)

cookies={}
cookies["_censeid"]=""
# sids=[239247877656260394,248428014489979204,265754401946389642,242743334768288078,246638669824291507,263124544565138727,248175596605161600,240372644530355698,265913697062034046,246477390474268801,247419501742916420,239792583418303990,248243823626382700,264524577701191847,242980071846761092,246485548086247616,239981476043127194,264622816632920664,245829039630904508,243146918981321576,245339276843085405,239792583418303990]

# results = []
# for x in sids:
# 	result = json.loads(exct( "/trade/backend/sync/single?userId=10693&tid=%s"%x,"",cookies))
# 	orders = result["data"]['tb']['orders']
# 	append = False
# 	for y in orders:
# 		refund = y['refundStatus']
# 		if refund != 'NO_REFUND':
# 			append = True
# 	if append:
# 		print result["data"]['tb']['tidStr']

# print results

# file = open('/Users/gongdaoyan/Documents/sublime Text/python/result','w')
# file.write(json.dumps(results))
# {
#   "data": [
#     {
#       "companyId": 8131,
#       "id": 4682,
#       "outSid": "9991053489",
#       "pid": 1543,
#       "seq": 4,
#       "table": "multi_packs_print_trade_log_detail"
#     },
#     {
#       "companyId": 8131,
#       "id": 4681,
#       "outSid": "9991043987",
#       "pid": 1543,
#       "seq": 3,
#       "table": "multi_packs_print_trade_log_detail"
#     },
#     {
#       "companyId": 8131,
#       "id": 4683,
#       "outSid": "9991045007",
#       "pid": 1543,
#       "seq": 5,
#       "table": "multi_packs_print_trade_log_detail"
#     },
#     {
#       "companyId": 8131,
#       "id": 4680,
#       "outSid": "9991044908",
#       "pid": 1543,
#       "seq": 2,
#       "table": "multi_packs_print_trade_log_detail"
#     }
#   ],
#   "qTime": 44,
#   "result": 1
# }






cookies={}
# cookies["_uab_collina"]="153097339939374400500337"
# cookies["_umdata"]="535523100CBE37C3B90C90BC19C92F6B56BD191A7D69C322A392F39188B6320E67A8A3FD63A7D1EBCD43AD3E795C914CEEF3F1BCEBDEDCA8636C8B5071603B71"
# cookies["_ati"]="8446340310938"
# cookies["h_identify"]="139351ad57a5f3c2388334391e5d9570"
# cookies["identify"]="34ecd02573e9dd64a3ce57bde37d1f31"
# cookies["JSESSIONID"]="78F333CFCBD4EC017BAFA953836267BE"
# cookies["auth"]="ceb8afff52902ce39286a4c2f4a85563099e50e2_42998646346240"
# cookies["safe_ip"]="192.168.59.250"
# cookies["safe_identify"]="%E9%BE%9A%E9%81%93%E7%87%95"
# cookies["safe_sign"]="3e2a3d4e672acd572d1904dcfe7565e6"
# cookies["safe_time"]="1542251534185"
# cookies["safe_user"]="%E9%BE%9A%E9%81%93%E7%87%95"
# cookies["super_memSessionId1"]="5640227d06083ac89558110c8ca815df224993a1c2d5c7d715122eb25c6ae0ac0a196ebc6441f0798b379ffb01c9021113de771c83269195e454f5edbc688f40"
# cookies["superuseragent1"]="4003a5039f0e8f7a5ba7cc0603669c089e9e77724e6c62093d768ecdbefa044b86b436eb44ec9d23c5d3d5d0059455967db2083301dcb8d1ee8dcd062c830a8cb8bcb576a87cde656d1383b848ef44b2971c285beb125bc9177f0ba9e1e3637bc0cdfa7ecef7cc549950b2293c3d7c98e43da585df59ac74d6450cf87ea8c6ef"
# cookies["visitorId"]="140336565449216"
cookies["_censeid"]=""
# cookies["_shatg"]="13eae6eb-bed6-4697-999d-32d839373a3e"

# # data = {"timeType":"getterTime","startTime":1541654460025,"endTime":1542259260025,"pageNo":1,"pageSize":100,"wlbTemplateTypes":"0,2","branchTaobaoId":""}
# count = 0
# a = json.loads(exct( "/wms/goodsSectionInventory/list?async=false&userId=5044&warehouseId=1&queryType=outerId&pageNo=1&pageSize=100",{},cookies))
# print a
# for x in a.get("data").get("list"):
# 	print exct( "/wms/goodsSectionInventory/update?goodsSectionId=1&goodsSectionCode=A22121123&sysSkuId=%s&sysItemId=%s&num=9999&async=false"%(x.get('sku').get('sysSkuId'),x.get('sku').get('sysItemId')),{},cookies)

pageNo = 1
while True:
	print pageNo
	a = json.loads(exct('/trade/consign/detail?api_name=trade_consign_detail&isError=1&pageNo=%s&queryType=0&field=upload_time&order=desc&pageSize=100'%pageNo,{},cookies)).get('data').get('list')
	needBreak = True
	sids = []
	for x in a:
		needBreak = False
		sids.append(x.get('sid'))
	if needBreak:
		break
	print exct('/trade/consign/upload/again?sids=%s'%','.join(sids),{},cookies)
	pageNo = pageNo + 1





