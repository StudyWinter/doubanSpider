#-*- coding = utf-8 -*-
#@Time: 2020/9/19 15:26
#@Author: Winter
#@File: requestsTest.py
#@Software: PyCharm

#requests是请求网络响应的函数库
import requests
#re时正则表达式的函数库
import re
#保存文件
import csv

#请求网址
url = "https://www.xust.edu.cn/index/tzgg.htm"

#设置头部和cookie，反爬，伪装
head = {"Content-Type": "text/html;charset=utf-8","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

r = requests.get(url = url,headers = head)

r.encoding = "utf-8"        #编码
html = r.text
#print(html)

#正则表达式筛选,得到的类型是list类型的

#链接信息的正则表达式
info_link = re.findall(r'<li .*?><a href="../info(.*?)" target="_blank"',html)
#标题信息的正则表达式
info_title = re.findall(r'<a .*?>(.*?)</a><span>',html)
#时间信息的正则表达式
info_time = re.findall(r'</a><span>(.*?)</span></li>',html)

# for item in info_link:
#     print(item)

#列表打包迭代
rows = zip(info_link,info_title,info_time)

with open("xust.csv","w",newline="",encoding="utf-8-sig")as csvfile:
    writer = csv.writer(csvfile)
    for val in rows:                  #按行写入
        writer.writerow(val)