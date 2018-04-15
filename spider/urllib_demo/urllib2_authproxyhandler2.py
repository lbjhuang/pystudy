#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib2
import os
#使用自定义opener处理器来请求，这样可以设置代理服务器等自定义功能
# 获取系统环境变量的授权代理的账户和密码
proxyuser = os.environ.get("proxyuser")
proxypasswd = os.environ.get("proxypasswd")

# 授权的代理账户密码拼接
authproxy_handler = urllib2.ProxyHandler({"http" : proxyuser+":"+proxypasswd+"@114.215.104.49:16816"}) #设置私密代理服务器
#authproxy_handler = urllib2.ProxyHandler({"http" : "114.215.104.49:16816"})   #设置开放代理服务器，开放代理不稳定，一般不用，私密代理稳定，但要钱

# 构建一个自定义的opener
opener = urllib2.build_opener(authproxy_handler)

# 构建请求
request = urllib2.Request("http://www.baidu.com/")

# 使用自定义的代理处理器来请求，获取响应
response = opener.open(request)

# 打印内容
print response.read()

