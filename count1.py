#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import time
# def parseTime(dateStr):
#     timeArray = time.strptime(dateStr, '%Y-%m-%d %H:%M:%S.%f')
#     print timeArray.time()
#     timeStamp = int(time.mktime(timeArray)) * 1000
#     print(timeStamp)
#     return timeStamp
import arrow
def parseTime(dateStr):
	print arrow.get(dateStr).timestamp*1000

parseTime('2018-10-31 23:58:52.395')