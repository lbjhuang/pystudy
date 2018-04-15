#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2, urllib
#post 请求有道翻译

url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
headers = {
            "User-Agent": "User-Agent:Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Accept":"application/json, text/javascript, */*; q=0.01",
            "X-Requested-With":"XMLHttpRequest",
            "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8",
           }

keyword = raw_input("请输入需要查询的关键字")

formdata = {
"i":keyword,
"from":"AUTO",
"to": "AUTO",
"smartresult":"dict",
"client":"fanyideskweb",
"doctype":"json",
"version":2.1,
"keyfrom":"fanyi.web",
"action":"FY_BY_REALTIME",
"typoResult":"false"
}

#参数是一个字典,并urlencode编码，
formdata = urllib.urlencode(formdata)

request = urllib2.Request(url, data= formdata, headers=headers)
result = urllib2.urlopen(request)

print result.getcode()
print result.read()
print result.info()