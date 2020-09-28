#-*- coding = utf-8 -*-
#@Time: 2020/9/15 15:48
#@Author: Winter
#@File: testXwlt.py
#@Software: PyCharm

import xlwt


# workbook = xlwt.Workbook(encoding="utf-8")      #1创建workbook对象
# worksheet = workbook.add_sheet("sheet1")        #2.创建worksheet  创建工作表
# worksheet.write(0,0,"hello")                    #3写入数据  在第0行 0列写入hello
# workbook.save("student.xls")                    #4保存数据表

#将99乘法表写入到Excel中

workbook = xlwt.Workbook(encoding="utf-8")        #1创建workbook对象
worksheet = workbook.add_sheet("sheet1")          #2.创建worksheet  创建工作表

i = 0
j = 0
for i in range(0,9):
    for j in range(0,i+1):
        worksheet.write(i,j,"%d * %d = %d"%(j+1,i+1,(j+1)*(j+1)))

workbook.save("九九乘法表.xls")