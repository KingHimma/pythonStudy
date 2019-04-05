#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import time
import datetime
"""
Python 操作文件夹
"""

def files_and_dirs_list(dir_path):
    """
    遍历文件夹及文件夹下所有文件（包括文件夹）
    :param dir_path: 文件夹路径
    :return:
    	root 所指的是当前正在遍历的这个文件夹的本身的地址
    	dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    	files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
    """
    for root, dirs, files in os.walk(dir_path):
        print(root)
        print(files)

def all_files(dir_path):
    """
    输出文件夹下所有文件名（不包括文件夹）
    :param dir_path: 文件夹路径
    :return:
    """
    for file in os.listdir(r'/Users/gongdaoyan/Desktop/test'):
        print(file)

def del_dir(dir_path):
    """
    删除文件夹及内容
    :param dir_path:
    :return:
    """
    import shutil
    shutil.rmtree(dir_path)



def deleteFile(filePath):
    print filePath
    os.remove(filePath)


def copy_dir(olddir_path,newdir_path):
    """
    复制文件夹，olddir和newdir都只能是文件夹，且newdir必须不存在
    :return:
    """
    if os.path.exists(newdir_path):
        shutil.rmtree(newdir_path)

    shutil.copytree(olddir_path, newdir_path)

import hashlib
import os

# 获取文件MD5值
def get_md5_01(file_path):
  md5 = None
  if os.path.isfile(file_path):
    f = open(file_path,'rb')
    md5_obj = hashlib.md5()
    md5_obj.update(f.read())
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
  return md5


#获取文件后缀
def file_extension(path):
    return os.path.splitext(path)[1]

def TimeStampToTime(timestamp):
    timeStruct = time.localtime(timestamp)
    return time.strftime('%Y-%m-%d %H:%M:%S',timeStruct)
    # return time.strftime('%Y-%m-%d',timeStruct)




'''
获取文件的创建时间
'''
def get_FileCreateTime(filePath):
    filePath = unicode(filePath,'utf8')
    t = os.path.getctime(filePath)
    return TimeStampToTime(t)


import sys
import xlrd
import xlwt
import sys;
reload(sys);
sys.setdefaultencoding('utf8')
from datetime import datetime
import json
import requests


## 执行请求
def exct(url, date = {}, cookies = ''):
    print url
    headers = {'kbn-version':'6.3.0'}
    return requests.post(url, data=json.dumps(date), cookies = cookies,headers= headers).content

def eget(url, params):
    headers = {
                  "Accept": "application/json, text/javascript, */*; q=0.01",
                  "Accept-Encoding": "gzip, deflate, br",
                  "Accept-Language": "zh-CN,zh;q=0.9",
                  "Cache-Control": "no-cache",
                  "Connection": "keep-alive",
                  "Cookie": "BAIDUID=901E981540F7DAA25AC23ED75E996CE1:FG=1; PSTM=1530768460; pan_login_way=1; PANWEB=1; BIDUPSID=901E981540F7DAA25AC23ED75E996CE1; MCITY=-179%3A; BDCLND=dfnU1OnEre6qU252Sji5l9mpmFszK3afwdceMS9%2BEeg%3D; BDUSS=U9KRzllUllTdVpyRFBQdVN4aHVBbEZjU3ZYZVdsV3Rocnl5N0h4bGdSUzVFczljRUFBQUFBJCQAAAAAAAAAAAEAAAAZYjw6Z7jf0KHD9wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALmFp1y5hadcb; STOKEN=dfbaf5e877c64c555e28451f13d8c1f7320a396ba04bad30eb985891e5130d51; SCRC=08fd967a6a0688316ffdc0f1bc4362ed; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; delPer=0; PSINO=1; H_PS_PSSID=1451_21105_19898_28773_28724_28557_28584_28603_28605; cflag=13%3A3; Hm_lvt_7a3960b6f067eb0085b7f96ff5e660b0=1554482624,1554486222,1554486301,1554486306; Hm_lpvt_7a3960b6f067eb0085b7f96ff5e660b0=1554486306; PANPSC=2116471357268693968%3AtLScB1szpOSsFmb%2FIEp3caeLxxr5GVy0jQA2R8iSPbyXNJQJh01fm8ZDtQAWdbTjEzh0OPEF2WkCXCidXDQoj4M5YEyYudt6oXX3yqgRkTeAzDutBADgO0NnO1jfh%2Fj1Ma5pkKMC7NZipl3L3NnXecV35zM8E1i3No8m%2ByaHSIqMVj%2BP8sFRaA%3D%3D",
                  "DNT": "1",
                  "Host": "pan.baidu.com",
                  "Pragma": "no-cache",
                  "Referer": "https://pan.baidu.com/disk/home?errno=0&errmsg=Auth%20Login%20Sucess&&bduss=&ssnerror=0&traceid=&",
                  "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
                  "X-Requested-With": "XMLHttpRequest"
                }
    r = requests.get(url, params = params, headers = headers)
    return r.json()

sys_encoding = sys.getfilesystemencoding()
def printcn(msg):
    print(msg.decode('utf-8').encode(sys_encoding))

#JSON 打印中文不乱吗
def printJsonCn(msg):
    print json.dumps(msg, encoding="UTF-8", ensure_ascii=False)


params = {"order": "time",
                "desc": "1",
                "showempty": "0",
                "web": "1",
                "page": "1",
                "num": "500",
                "dir": "/照片/17年毕业前（可能存在重复）",
                "t": "0.3909410298330167",
                "channel": "chunlei",
                "web": "1",
                "app_id": "250528",
                "bdstoken": "7ecb4534fe203e676430651bf997ddf6",
                "logid": "MTU1NDQ4NjMwOTAyNDAuMDIwMTY0Njk1NTgxOTMxOTAy",
                "clienttype": "0",
                "startLogTime": "1554486309024"
                }

def getAllWPfileWithDirs(dir, count):
    wp_files = {}
    for x in xrange(1,10000):
        params["dir"] = dir
        params["page"] = x
        printcn(dir)
        print x
        allFilesWJJ = eget("https://pan.baidu.com/api/list",params)
        file1 = allFilesWJJ.get("list")
        if len(file1) == 0:
            break
        for file2 in file1:
            count = count + 1
            server_file_name = file2.get("server_filename")
            local_mtime = file2.get("local_mtime")
            newFileName = TimeStampToTime(local_mtime)+"_%s"%count+file_extension(server_file_name)
            wp_files[server_file_name] = newFileName
            # print (count, len(wp_files))
    return wp_files


## 拉取网盘中的本地时间
def getAllWPfile():
    allFileMap = {}
    count = 0
    dirs = ["/照片/19"]
    for x in dirs:
        ## dict 合并
        allFileResult = getAllWPfileWithDirs(x, count)
        allFileMap = dict(allFileMap.items() + allFileResult.items())
        count = len(allFileMap)
    # printJsonCn(allFileMap)
    return allFileMap


def rename(dir_path, desc_path):
    allFileMap = getAllWPfile()
    printJsonCn(allFileMap)
    for root, dirs, files in os.walk(r''+dir_path):
        printcn(root)
        for x in files:
            if '.DS_Store' != x  :
                if  '男.jpg' != x:
                    if '女.jpg' != x:
                        printcn(x)
                        oldname = root +'/'+ x
                        dirName = allFileMap[x].split('-')[0]
                        newpath = desc_path +'/'+ dirName
                        isExists=os.path.exists(newpath)
                        # 判断结果
                        if not isExists:
                            # 如果不存在则创建目录
                            # 创建目录操作函数
                            os.makedirs(newpath)
                        print newpath+"/"+allFileMap[x]
                        shutil.copyfile(oldname,newpath+"/"+allFileMap[x])
                        os.remove(oldname)

## 比较两个文件夹中MD5相同的文件 并删除后面的
def compaleAndDelete(paths):
    allFilesMD5 = []
    for dir_path in paths:
        for root, dirs, files in os.walk(r''+dir_path):
            printcn(root)
            for x in files:
                path = root +'/'+ x
                md5_result = get_md5_01(path)
                print(path, get_FileCreateTime(path))
                if md5_result in allFilesMD5:
                    printcn('remove -->'+ path)
                    os.remove(path)
                allFilesMD5.append(md5_result)



import shutil

if __name__ == '__main__':
    paths=[r'/Users/gongdaoyan/Desktop/test/1']
    # dir_path=r'/Users/gongdaoyan/Desktop/test/2'
    compaleAndDelete(paths)
    # printJsonCn(getAllWPfile())
    # 遍历文件夹下所有文件
    # files_and_dirs_list(dir_path)
    # #遍历文件夹下所有文件，不包括文件夹
    # all_files(dir_path)
    # # 删除文件夹及内容
    # del_dir(dir_path)
    # #复制文件夹
    # copy_dir(olddir_path,newdir_path)







