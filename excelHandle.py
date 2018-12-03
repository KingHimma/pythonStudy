# -*- coding: utf-8 -*-
#!/usr/bin/env python3
import sys
import xlrd
import xlwt
from datetime import date,datetime


# reload(sys)
# sys.setdefaultencoding('utf-8')


def read_excel():
	#文件位置
	excelFile=xlrd.open_workbook(r'/Users/gongdaoyan/Desktop/origin.xlsx')
	sheet1 = excelFile.sheet_by_index(0)
	colnum = sheet1.nrows
	postionCodes = []
	allPostionCodes = []
	outter_ids = []## 商家编码
	nums =[]
	for index in range(1,colnum):
		rows = sheet1.row_values(index)
		postionCode = rows[7]
		if postionCode == 'X-1-1-1-1':
			postionCode = 'X-1-1-1';
		split = postionCode.split('-')
		split[2] = split[2].rjust(3,'0')
		postionCode = '-'.join(split)
		if postionCode not in postionCodes:
			postionCodes.append(postionCode)
		outter_ids.append(rows[2])
		allPostionCodes.append(postionCode)
		nums.append(rows[6])

	## 货位编码
	outFile = xlwt.Workbook()
	sheet1 = outFile.add_sheet('sheet1',cell_overwrite_ok=True)
	sheet1.write(0,0,'仓库编码'.decode('utf-8'))
	sheet1.write(0,1,'库区'.decode('utf-8'))
	sheet1.write(0,2,'排'.decode('utf-8'))
	sheet1.write(0,3,'层'.decode('utf-8'))
	sheet1.write(0,4,'位置号'.decode('utf-8'))
	count = 1
	for x in postionCodes:
		splitData = x.split('-')
		sheet1.write(count,0,'A')
		sheet1.write(count,1,splitData[0])
		sheet1.write(count,2,splitData[1])
		sheet1.write(count,3,splitData[2])
		sheet1.write(count,4,splitData[3])
		count = count + 1;
	outFile.save(r'/Users/gongdaoyan/Desktop/postionCodes.xls')


	outFile1 = xlwt.Workbook()
	sheet1 = outFile1.add_sheet('sheet1',cell_overwrite_ok=True)
	sheet1.write(0,0,'商家编码'.decode('utf-8'))
	sheet1.write(0,1,'生成批次'.decode('utf-8'))
	sheet1.write(0,2,'货位编码'.decode('utf-8'))
	sheet1.write(0,3,'盘点数'.decode('utf-8'))
	sheet1.write(0,4,'次品'.decode('utf-8'))
	count = 2
	index = 0
	for x in outter_ids:
		code = allPostionCodes[index]
		num = nums[index]
		sheet1.write(count,0,x)
		sheet1.write(count,1,'')
		sheet1.write(count,2,code)
		sheet1.write(count,3,num)
		sheet1.write(count,4,'否'.decode('utf-8'))
		count = count + 1;
		index = index + 1;
	outFile1.save(r'/Users/gongdaoyan/Desktop/postionCodes1.xls')

read_excel()
