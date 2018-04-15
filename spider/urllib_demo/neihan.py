#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2, re, os

class Spider:
    def __init__(self):
        #初始化
        self.page = 1
        #爬取开关
        self.switch = True

    def loadPage(self):
        print "正在爬取页面....."
        url = "http://www.neihan8.com/article/list_5_" + str(self.page) + ".html"
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)

        #获取每页源码字符串
        html = response.read()
        #创建正则表达式
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)
        #匹配div获取文字内容
        content = pattern.findall(html)

        # 调用dealPage() 处理段子里的杂七杂八
        self.dealPage(content)

    def dealPage(self,content):
        for item in content:
            #替换一些字符串为空
            item = item.replace("<p>", "").replace("</p>", "").replace("<br>", "").replace("<br />","")
            #item = item.decode("gbk")
            #处理完了将内容调用写入文件方法写入文件
            self.writeContent(item)

    def writeContent(self, content):
        savePath = "./res/neihanduanzi"
        if (os.path.exists(savePath) == False):
            os.makedirs(savePath)
        fileName = "duanzi.txt"
        with open(savePath+"/" + fileName, 'a') as f:
            print ("正在保存爬取的内容到res目录下neihanduanzi文件夹中......")
            f.write(content)


    #控制是否爬取
    def startWork(self):
        while self.switch:
            self.loadPage()
            command = raw_input("停止请按q:")
            if(command == 'q'):
                self.switch = False
            self.page += 1
        print "Thank you ^_^"

if __name__ == "__main__":
    duanziSpider = Spider()
#    duanziSpider.loadPage()
    duanziSpider.startWork()