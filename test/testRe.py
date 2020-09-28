#-*- coding = utf-8 -*-
#@Time: 2020/9/14 21:58
#@Author: Winter
#@File: testRe.py
#@Software: PyCharm


#正则表达式：字符串模式(判断字符串是否符合一定的标准) 搜索、验证

import re
#1创建模式对象

pat = re.compile("AA")   #此处的AA，是正则表达式，用来去验证其他的字符串
#m = pat.search("CBA")    #search后面的字符串是被校验的内容
#m = pat.search("ABCAAA")  #<_sre.SRE_Match object; span=(3, 5), match='AA'>   左闭右开区间
#m = pat.search("ABCAAACCAAAA") #<_sre.SRE_Match object; span=(3, 5), match='AA'>   进行比对查找，第一次出现的AA



#2没有模式对象
#m = re.search("asd","Aasd")   #前面的字符串是规则（模版），后面的字符串是被校验的对象

#print(m)

# print(re.findall("a","ASDaDFsa"))   #前面字符串是规则，后面是被校验的。['a', 'a']
#
# print(re.findall("[A-Z]","ABCDabcdZ"))   #['A', 'B', 'C', 'D', 'Z']
#
# print(re.findall("[A-Z]+","ABCabcdSCZcvSD"))  #['ABC', 'SCZ', 'SD']


#sub
print(re.sub("a","A","abcdcasdf"))    #用A来替换a.在第三个字符串中查找

#建议在正则表达式中，在被比较的字符串前面加上r。r是防止转义字符生效，不用担心转义字符的问题
a = r"\aaacv'\'"
print(a)