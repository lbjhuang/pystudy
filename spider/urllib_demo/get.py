#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2, urllib
#get 请求

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Mozilla..."}

keyword = raw_input("请输入需要查询的关键字")
wd = {"word": keyword}
#参数是一个字典,并urlencode编码，
wd = urllib.urlencode(wd)
#构造一个完整url
fullUrl = url + '?' +wd
print fullUrl

request = urllib2.Request(fullUrl, headers=headers)
html = urllib2.urlopen(request)

print html.getcode()

