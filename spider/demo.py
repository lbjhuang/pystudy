# -*- coding: UTF-8 -*-
import urllib2


result = urllib2.urlopen("http://www.baidu.com")
html = result.read()
print(html)