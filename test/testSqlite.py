#-*- coding = utf-8 -*-
#@Time: 2020/9/16 15:06
#@Author: Winter
#@File: testSqlite.py
#@Software: PyCharm

import sqlite3

#1连接数据库
# conn = sqlite3.connect("test.db")   #默认在当前路径创建  打开或者创建数据库文件
#
# print("open database successfully")


#2创建数据表
# conn = sqlite3.connect("test.db")   #默认在当前路径创建  打开或者创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()      #1获取一个游标
#
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real);
# '''
#
# c.execute(sql)         #2执行sql
# conn.commit()          #3提交
# conn.close()           #关闭数据过连接
#
# print("成功建表")


#3插入数据
# conn = sqlite3.connect("test.db")   #默认在当前路径创建  打开或者创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()      #1获取一个游标
#
# sql = '''
#     insert into company
#     (id,name,age,address,salary)
#     values(1,"李四",23,"陕西西安",8000)
# '''
#
# c.execute(sql)         #2执行sql
# conn.commit()          #3提交
# conn.close()           #关闭数据过连接
#
# print("插入数据成功")


#4查询数据
# conn = sqlite3.connect("test.db")   #默认在当前路径创建  打开或者创建数据库文件
# print("成功打开数据库")
#
# c = conn.cursor()      #1获取一个游标
#
# sql = '''
#     select * from company
# '''
#
# cursor = c.execute(sql)         #2执行sql
#
# #打印
# #print(cursor)
# for row in cursor:
#     print("id = ",row[0])
#     print("name = ",row[1])
#     print("age = ",row[2])
#     print("address = ",row[3])
#     print("salary = ",row[4],"\n")
#
#
#
# conn.close()           #关闭数据过连接
#
# print("查询数据成功")


#5删除数据
conn = sqlite3.connect("test.db")   #默认在当前路径创建  打开或者创建数据库文件
print("成功打开数据库")

c = conn.cursor()      #1获取一个游标

sql = '''
    delete from company where name ='%s'
    ''' %('zhangsan')

cursor = c.execute(sql)         #2执行sql


conn.close()           #关闭数据过连接

print("删除数据成功")
