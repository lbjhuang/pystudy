# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
import base64

from douban.settings import  USER_AGENTS
from douban.settings import  PROXIES

#反反爬虫策略:定义几个中间件类（随机用户代理和代理服务器等）
class RandomUserAgent(object):
    def process_request(self,request,spider):
        user_agent = random.choice(USER_AGENTS)
        request.headers.setdefault("User-Agent", user_agent)

class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXIES)
        if proxy['user_passwd'] is None:
            #没有代理验证用户的代理使用方式
            request.meta['proxy'] = "http://" + proxy['ip_port']
        else:
            #对账户密码进行base64转换
            base64_userpasswd = base64.b64encode(proxy['user_passwd'])
            # 对应到代理服务器的信令格式里
            request.headers['Proxy-Authorization'] = 'Basic ' + base64_userpasswd

            request.meta['proxy'] = "http://" + proxy['ip_port']
