# coding:utf-8
import urllib
import re

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    html = html.decode('utf-8')
    return html

def getImg(html):
    reg = r'data-original = "(.+?\.jpg)"'
    imgre = re.compile(reg)
    imglist = imgre.findall(html)
    return imglist

def downImg(pageNum, imglist):
    x = 0
    for imgurl in imglist:
        x += 1
        urllib.urlretrieve(imgurl, 'G:\images\Page%s_Num%s.jpg' % (pageNum, x))
        print '第%s页第%s张下载完成' % (pageNum, x)
    print '第%s页图片下载完成' % pageNum

imgNum = 0
pageNum = 1
while pageNum <= 2:
    url = 'http://www.win4000.com/zt/fengjing_%s.html' % pageNum
    print url
    html = getHtml(url)
    print html
    imglist = getImg(html)
    imgNum += len(imglist)
    print imglist
    downImg(pageNum, imglist)
    pageNum += 1
print '%s页图片共%s张下载完成' % (pageNum - 1, imgNum)
