# coding:utf-8
from bs4 import BeautifulSoup  # BeautifulSoup官网https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
import urllib
import pymysql  # python3及以上用pymysql，不能用MySQLdb

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    html = html.decode('gbk')
    return html

html_doc = getHtml('http://my.yingjiesheng.com/xuanjianghui.html')
html = BeautifulSoup(html_doc, 'html.parser')
# 'lxml'、'html5lib'、和 'html.parser'三种解析器详见https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html#id47
# print(html.prettify())
addressTags = html.select('td[width="80"] > a[target="_blank"]')
addresses = [str(x) for x in range(0,addressTags.__len__(),1)]
add = 0
for addressTag in addressTags:
    address = BeautifulSoup(addressTag.__str__(), 'html.parser').string
    addresses[add] = address
    print address,
    add += 1
print

try:
    db = pymysql.connect("localhost", "root", "root", "test",charset="utf8")
    cursor = db.cursor()  # 创建游标
    print len(addresses)
    for address in addresses:
        sql = "insert into tb_xuanjiang(cityName) VALUES ('%s')" % address
        cursor.execute(sql)
        db.commit()
    print '数据库%s条数据插入完成' % len(addresses)
except Exception,e:
    db.rollback()
    print e.message
db.close()

