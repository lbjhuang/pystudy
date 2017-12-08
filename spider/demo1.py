# -*- coding: UTF-8 -*-
import urllib2


re_headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
}
#构造请求对象，设置请求头
request = urllib2.Request("http://www.baidu.com", headers=re_headers)
#向指定的url地址发送请求，并返回服务器响应的类文件对象
response = urllib2.urlopen(request)
# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串
print response.read()
#返回状态码
print response.getcode()
#返回实际数据的实际URL，防止重定向问题
print response.geturl()
#返回服务器响应的http报头
print response.info()