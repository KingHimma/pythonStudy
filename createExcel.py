#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 二维数组生成excel

import sys
import xlrd
import xlwt
from datetime import date,datetime


def createExcel(excelData, fileName):
	outFile1 = xlwt.Workbook()
	sheet1 = outFile1.add_sheet('sheet1',cell_overwrite_ok=True)
	index = 0;
	for x in excelData:
		index1 = 0
		for y in x:
			sheet1.write(index,index1,('%s'%y).decode('utf-8'))
			index1 = index1 + 1
		index = index + 1
	outFile1.save(r'/Users/gongdaoyan/Desktop/%s.xls'%fileName)



company=[[1,2,3],[5,3,3],[7,7,7]]
createExcel(company, 'test')

