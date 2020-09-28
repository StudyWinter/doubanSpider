#-*- coding = utf-8 -*-
#@Time: 2020/9/13 9:50
#@Author: Winter
#@File: spider.py
#@Software: PyCharm


#引入模块
from bs4 import BeautifulSoup    #网页解析，获取数据
import re      #正则表达式，进行文字匹配
import urllib.request,urllib.error   #制定URL，获取网页数据
import xlwt    #进行Excel操作
import sqlite3 #进行sqlite3数据库操作


def info():
    baseurl = "https://movie.douban.com/top250?start="

    #1.爬取网页
    datalist = getData(baseurl)



    #3.保存数据
    savePath = "豆瓣电影Top250.xls"
    saveData(datalist,savePath)
    #askURL("https://movie.douban.com/top250?start=")

    #3.保存到数据库中去
    # dbPath = "movie.db"
    # saveData2DB(datalist,dbPath)     #保存到数据库中



#全局变量    创建正则表达式对象，表示规则（字符串的模式）

#影片详情链接的规则
findLink = re.compile(r'<a href="(.*?)">')
#影片图片的链接规则
findImaSrc = re.compile(r'<img.*src="(.*?)"',re.S)    #re.S让换行符包含在字符中
#影片片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
#评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
#找到概况
findInq = re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd = re.compile(r'<p class="">(.*?)</p>',re.S)     #re.S让换行符包含在字符中


#1爬取网页
def getData(baseurl):
    datalist = []


    for i in range (0,10):           #调用获取页面信息的函数10次
        url = baseurl+str(i*25)
        html = askURL(url)           #保存获取到的网页原码

        # 2.逐一解析数据
        soup = BeautifulSoup(html,"html.parser")       #解析
        #提取
        for item in soup.find_all("div",class_="item"):         #查找符合要求的字符串，形成列表
            #print(item)                  #测试查看电影item
            data = []                     #保存一部电影的所有信息
            item = str(item)              #变成字符串



            #影片详情的超链接
            link = re.findall(findLink,item)[0]            #re库用来通过正则表达式查找指定的字符串
            data.append(link)                              #添加链接

            imgSrc = re.findall(findImaSrc,item)[0]
            data.append(imgSrc)                            #添加图片

            titles = re.findall(findTitle,item)
            if (len(titles)==2):
                ctitle = titles[0]
                data.append(ctitle)                            #添加中文名
                otitle = titles[1].replace("/","")            #去掉/
                data.append(otitle)                           #添加外国名
            else:
                data.append(titles[0])
                data.append(" ")                              #外国名留空

            rating = re.findall(findRating,item)[0]
            data.append(rating)                             #添加打分

            judgeNum = re.findall(findJudge,item)[0]
            data.append(judgeNum)                           #添加评价人数

            inq = re.findall(findInq,item)
            if len(inq)!=0:
                inq = inq[0].replace("。","")              #去掉句号
                data.append(inq)                                #添加概述
            else:
                data.append(" ")                          #留空

            bd = re.findall(findBd,item)[0]
            bd = re.sub('<br(\s+)?/>(\s+)?'," ",bd)       #去掉<br/>
            bd = re.sub('/'," ",bd)                       #替换/
            data.append(bd.strip())                       #去掉前后的空格

            datalist.append(data)                         #处理好的一部电影信息放入datalist

    return datalist



#得到指定一个URL的网页内容
def askURL(url):
    #用户代理，告诉豆瓣服务器，我们是什么类型的机器，浏览器（本质上是告诉浏览器，我们可以接受什么水平的文件内容）

    #头部信息，模拟浏览器头部信息，向豆瓣浏览器发送消息
    head={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
    #请求
    request = urllib.request.Request(url,headers=head)
    #存储
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html




#3保存数据
def saveData(datalist,savePath):
    print("save......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 1创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250",cell_overwrite_ok=True)  # 2.创建worksheet  创建工作表  cell_overwrite_ok=True覆盖以前的内容

    col = ("电影详情链接","图片链接","影片中文名","影片外国名","评分","评价数","概况","相关信息")
    for i in range(0,8):
        sheet.write(0,i,col[i])              #写入列表

    for i in range(0,250):
        print("第%d条"%(i+1))
        data = datalist[i]
        for j in range(0,8):
            sheet.write(i+1,j,data[j])

    book.save(savePath)


#3保存到数据库中
def saveData2DB(datalist,dbPath):
    #1创建数据库
    init_db(dbPath)

    #2连接数据库
    conn = sqlite3.connect(dbPath)
    cursor = conn.cursor()            #获取一个游标

    #3对电影信息进行解析，并插入到数据库中
    for data in datalist:
        for index in range(0,len(data)):
            if index==4 or index==5:
                continue
            #在数据前后加上引号,数值的不需要添加引号
            data[index] = '"' + data[index] + '"'
        sql = '''
                    insert into movie250(
                        info_link,pic_link,cname,ename,score,rated,introduction,info
                    )
                    values (%s)'''%",".join(data)    #每一个data的数据用,连接起来
        print(sql)
        cursor.execute(sql)                 #执行SQL语句
        conn.commit()                       #执行完就提交一次
    cursor.close()
    conn.close()

    print(".....")


#4.创建数据库
def init_db(dbPath):

    #建表语句
    sql = '''
            create table movie250(
            id integer primary key autoincrement,
            info_link text,
            pic_link text,
            cname varchar,
            ename varchar,
            score numeric,
            rated numeric,
            introduction text,
            info text
            )
            
    '''   #创建数据表
    conn = sqlite3.connect(dbPath)    #默认在当前路径创建  打开或者创建数据库文件
    cursor = conn.cursor()            #获取一个游标
    cursor.execute(sql)               #执行SQL,创建数据表

    conn.commit()                     #提交
    conn.close()                      #关闭数据库


#当程序执行时
if __name__ =="__main__":
    #调用函数
    info()

    #测试建表语句
    #init_db("movieTest.db")

    print("爬取完毕......")