#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2, urllib, random, os

# 百度贴吧
# 可以是User-Agent列表，也可以是代理列表
ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; rv2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

#爬页面
def getPage(fullUrl):
    request = urllib2.Request(fullUrl)
    request.add_header("User-Agent", user_agent)
    response = urllib2.urlopen(request)
    return response.read()

#爬取结果写入文件
def writeFile(html, savePath, fileName):
    print "正在保存"+fileName
    with open(savePath+"/"+fileName, 'w') as f:
        f.write(html)
        print "-"*50

#做爬取操作整个流程
def doSpider(url, startPage, endPage):
    for i in range(startPage, endPage):
        pn = (i - 1) * 50
        fullUrl = url + "&pn=" + str(pn)
        fileName = "page"+str(i)
        savePath = "./res/tiba"

        if(os.path.exists(savePath) == False):
            os.makedirs(savePath)

        print "开始爬第" + str(i) + "页"
        html = getPage(fullUrl)
        writeFile(html, savePath, fileName)

    print "爬去完毕，文件保存在/res中，谢谢使用"


if __name__ == "__main__":
    kw = raw_input("请输入要爬去的贴吧名字：")
    startPage = int(raw_input("开始页面是："))
    endPage = int(raw_input("结束页面是："))

    url = "https://tieba.baidu.com/f"  # "https://tieba.baidu.com/f?kw=篮球ie=utf-8&pn="
    kw = urllib.urlencode({"kw": kw})
    doUrl = url + "?" + kw
    doSpider(doUrl, startPage, endPage)
