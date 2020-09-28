#-*- coding = utf-8 -*-
#@Time: 2020/9/14 16:04
#@Author: Winter
#@File: testbs.py
#@Software: PyCharm

'''
BeautifulSoup4将复杂HTML文档转换成复杂的树形结构，每个结点都是python的对象，所有的对象可以归纳为4种:
- Tag
- NavigableString
- BeautifulSoup
- Comment

'''

from bs4 import BeautifulSoup

file = open("./baidu.html","rb")    #打开文件
html = file.read().decode("utf-8")                  #读到内存里作为HTML文档
#解析文件
bs = BeautifulSoup(html,"html.parser")     #树形结构

# print(bs.title)                     #输出title    <title>百度一下，你就知道 </title>
# print(bs.a)                         #输出第一个a标签
# print(bs.head)                      #输出第一个head标签
# print(type(bs.head))                 #<class 'bs4.element.Tag'>

#1.Tag 标签及其内容：拿到它所找到的第一个内容


# print(bs.title.string)                #百度一下，你就知道
# print(type(bs.title.string))          #<class 'bs4.element.NavigableString'>


#2.NavigableString 标签里的内容（字符串）


# print(bs.a.attrs)                     #用字典的形式输出a标签的属性值
#
#
# print(type(bs))                        #<class 'bs4.BeautifulSoup'>

#3.BeautifulSoup 表示整个文档
# print(bs.name)                         #[document]
#
# print(bs.a.string)
# print(type(bs.a.string))               #<class 'bs4.element.Comment'>
#4.Comment 是一个特殊的NavigableString,输出内容不包含注释符号


#-------------------------------------------------------------------------------------------------

#文档的遍历

# print(bs.head.contents)           #拿到head里面的内容
# print(bs.head.contents[1])         #拿到第1个元素


#文档的搜索

#1.find_all()   找到所有
#字符串过滤：会查找与字符串完全匹配的内容，必须完全一样  a
# t_list = bs.find_all("a")
# print(t_list)

import re
#正则表达式搜搜索：使用search()方法来进行匹配
#t_list = bs.find_all(re.compile("a"))      #匹配带字符a的

# #方法：传入一个函数(方法)，根据函数的要求来搜索:标签中有name的  (了解)
# def name_is_exists(Tag):
#     return Tag.has_attr("name")
#
# t_list = bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

#print(t_list)



#2.kwarys    参数

#t_list = bs.find_all(id="head")       #id

#t_list = bs.find_all(class_=True)     #有class...

# t_list = bs.find_all(href="http://news.baidu.com")
#
# for item in t_list:
#     print(item)



#3.text参数
#t_list = bs.find_all(text="hao123")
#t_list = bs.find_all(text=["hao123","地图","贴吧"])

# t_list = bs.find_all(text=re.compile("\d"))    #应用正则表达式来查找包含特定文本的内容(标签里的字符串)
# #
# for item in t_list:
#     print(item)


#4.limit 参数
# t_list = bs.find_all("a",limit=3)
#
# for item in t_list:
#     print(item)



#5.CSS选择器
#t_list = bs.select("title")     #通过标签来查找
#t_list = bs.select(".mnav")     #通过类名来查找
#t_list = bs.select("#u1")        #通过id来查找
#t_list = bs.select("a[class='bri']")    #通过标签里面的属性来查找
# t_list = bs.select("head > title")       #通过字标签来查找
#
# for item in t_list:
#     print(item)


# t_list = bs.select(".mnav~.bri")    #兄弟结点
# print(t_list[0].get_text())


