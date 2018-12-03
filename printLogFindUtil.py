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

def exct(url, date = {}, cookies = ''):
	return requests.post('http://gray.erp.superboss.cc/%s'%url, date, cookies = cookies ).content

cookies={}
cookies["_censeid"]="a2d332bff8f422097a6ecf326a1a341288a843c6"
sids = {}

## 需要在日志中搜索的单号信息
outSids = [71427713674384,71427715674383,71427719674381,71427717674382,71427713674379,71427711674380,71427717674377,71427715674378,71427719674376,71427711674375,71427719674277,71427713674275,71427716674274,71427711674276,71427710674272,71427718674273,71427712674271,71427714674270,71427716674269,71427718674268,71427712674515,71427715674514,71427717674513,71427711674511,71427719674512,71427715674509,71427717674508,71427713674510,71427713674505,71427711674417,71427719674418,71427712674501,71427713674416,71427715674415,71427712674412,71427710674413,71427718674414,71427714674411,71427716674410,71427719674507,71427718674409,71427718674503,71427711674506,71427716674504,71427710674502,71427714674500,71427716674047,71427712674049,71427718674046,71427714674048,71427719674296,71427717674297,71427711674295,71427714674294,71427716674293,71427718674292,71427710674291,71427712674290,71427714674289,71427716674288,71427710674286,71427718674287,71427712674285,71427717674283,71427715674284,71427710674470,71427713674280,71427711674281,71427715674279,71427719674282,71427717674278,71427712674469,71427714674468,71427716674467,71427717674462,71427715674463,71427710674465,71427713674464,71427718674466,71427710674229,71427716674226,71427714674227,71427712674228,71427718674230,71427719674461,71427713674223,71427718674225,71427711674224,71427714674557,71427717674221,71427715674222,71427711674554,71427718674555,71427716674556,71427713674553,71427715674552,71427719674550,71427717674551,71427713674299,71427715674298,71427717674565,71427713674567,71427710674564,71427715674566,71427714674562,71427712674563,71427716674561,71427712674558,71427710674601,71427718674560,71427718674602,71427710674559,71427712674600,71427713673799,71427715673798,71427717673797,71427711673795,71427719673796,71427714673794,71427716673793,71427719674480,71427712674474,71427719674475,71427711674479,71427715674477,71427717674476,71427713674478,71427716674472,71427712674394,71427718674471,71427714674473,71427716674392,71427714674393,71427714674388,71427712674389,71427716674387,71427710674390,71427718674391,71427718674386,71427711674525,71427714674524,71427710674385,71427710674521,71427716674523,71427718674522,71427714674519,71427712674520,71427718674517,71427710674516,71427716674518,71427718674490,71427710674489,71427712674488,71427714674487,71427716674486,71427718674485,71427711674484,71427717674481,71427713674483,71427715674482,71427710674658,71427712674657,71427714674656,71427716674655,71427713674652,71427711674653,71427719674654,71427717674650,71427715674651,71427710674535,71427717674099,71427713674534,71427717674532,71427715674533,71427719674531,71427711674530,71427713674529,71427715674528,71427717674527,71427719674526,71427713674341,71427715674340,71427717674339,71427719674338,71427711674337,71427713674336,71427715674335,71427718674334,71427712674332,71427710674333,71427714674576,71427712674577,71427716674575,71427719674574,71427713674572,71427711674573,71427715674571,71427717674570,71427719674569,71427711674568,71427718674428,71427710674427,71427712674426,71427717674424,71427719674423,71427714674425,71427711674422,71427715674420,71427713674421,71427718674701,71427717674419,71427716674349,71427710674700,71427718674348,71427714674345,71427710674347,71427712674346,71427719674343,71427716674764,71427711674342,71427717674344,71427710674762,71427712674761,71427718674763,71427710674757,71427716674759,71427714674760,71427714674755,71427713674751,71427719674753,71427711674587,71427713674586,71427715674585,71427718674584,71427712674582,71427714674581,71427710674583,71427718674579,71427716674580,71427718674758,71427710674578,71427712674756,71427717674754,71427711674752,71427715674750,71427715674199,71427717674198,71427719674197,71427711674196,71427713674195,71427711674667,71427713674666,71427719674668,71427715674665,71427718674664,71427712674662,71427710674663,71427714674661,71427716674660,71427718674659,71427717674438,71427719674437,71427711674436,71427713674435,71427716674434,71427718674433,71427714674430,71427710674432,71427716674429,71427712674431,71427719674545,71427714674543,71427718674541,71427716674542,71427712674544,71427712674539,71427710674540,71427714674538,71427710674804,71427716674537,71427718674536,71427712674803,71427714674802,71427716674801,71427715674397,71427719674395,71427718674800,71427711674399,71427717674396,71427713674398,71427717674711,71427719674710,71427711674709,71427717674706,71427713674708,71427715674707,71427712674704,71427719674705,71427716674702,71427714674703,71427718674621,71427716674622,71427712674619,71427710674620,71427714674618,71427713674614,71427716674617,71427710674615,71427718674616,71427715674613,71427718674678,71427712674676,71427714674675,71427710674677,71427717674674,71427719674673,71427713674671,71427711674672,71427717674669,71427717674612,71427715674670,71427719674611,71427717674607,71427713674609,71427711674610,71427719674606,71427715674608,71427711674605,71427716674603,71427714674604,71427719674687,71427711674686,71427717674688,71427713674685,71427718674683,71427710674682,71427716674684,71427712674681,71427714674680,71427716674679,71427713674850,71427719674499,71427711674498,71427715674496,71427713674497,71427717674495,71427710674494,71427712674493,71427714674492,71427716674491,71427716674721,71427718674720,71427710674719,71427712674718,71427714674717,71427718674715,71427716674716,71427715674712,71427711674714,71427715674905,71427713674713,71427710674903,71427718674904,71427712674902,71427714674901,71427716674900,71427713674548,71427711674549,71427717674546,71427715674547,71427712674860,71427714674859,71427710674856,71427718674857,71427716674858,71427715674854,71427712674855,71427717674853,71427719674852,71427711674851,71427715674731,71427717674730,71427719674729,71427711674728,71427713674727,71427715674726,71427717674725,71427710674724,71427712674723,71427714674722,71427716674698,71427718674697,71427712674695,71427710674696,71427715674694,71427717674693,71427719674692,71427711674691,71427713674690,71427715674689,71427713674732,71427711674733]
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


