#-*- coding = utf-8 -*-
#@Time: 2020/9/13 22:33
#@Author: Winter
#@File: testurllib.py
#@Software: PyCharm

import urllib.request

#获取一个get请求
# response = urllib.request.urlopen("https://cn.bing.com/")
# print(response)                             #<http.client.HTTPResponse object at 0x000001C13A1D2F98>
# print(response.read().decode('utf-8'))      #对获取的网页原码进行utf-8解码


#获取一个post请求   http://httpbin.org/  模拟用户登陆

import urllib.parse     #解析
# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")   #字节文件封装
# response = urllib.request.urlopen("http://httpbin.org/post",data= data)
# print(response.read().decode('utf-8'))

#获取一个get请求   timeout=1 超时,处理异常
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("timeout")


# response = urllib.request.urlopen("http://httpbin.org/get")
# print(response.status)          #状态码 200

# response = urllib.request.urlopen("http://douban.com")
# print(response.status)          #状态码 418   被发现是爬虫


# response = urllib.request.urlopen("https://cn.bing.com/")
# print(response.getheaders())

# response = urllib.request.urlopen("https://cn.bing.com/")
# print(response.getheader("date"))   #获取其中某一个信息


#伪装成浏览器，不让豆瓣发现,需要包装一下
#url = "http://www.douban.com"

# url = "http://httpbin.org/post"
# #伪装浏览器，用字典的结构包装
# headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
#
# data = bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
# req = urllib.request.Request(url,data=data,headers=headers,method="POST")     #请求对象
# response = urllib.request.urlopen(req)    #发送请求
# print(response.read().decode("utf-8"))



#伪装成浏览器，不让豆瓣发现,需要包装一下
url = "http://www.douban.com"
#伪装浏览器
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

req = urllib.request.Request(url,headers=headers)     #请求对象
response = urllib.request.urlopen(req)    #发送请求
print(response.read().decode("utf-8"))
