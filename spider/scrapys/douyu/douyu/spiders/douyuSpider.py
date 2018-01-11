# -*- coding: utf-8 -*-
#斗鱼美女图片爬虫
import scrapy
from douyu.items import DouyuItem
import json

class DouyumeimeiSpider(scrapy.Spider):
    name = "douyumeinv"
    allowed_domains = ["capi.douyucdn.cn"]
    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]    #框架会请求处理里面的url，把结果交个parse方法

    # 必须的函数，当拿到响应结果后再进入parse方法处理请求结果
    def parse(self, response):
        # 把json格式数据转成python格式，data段是列表
        data = json.loads(response.text)['data']
        for each in data:
            item = DouyuItem()
            item['nickname'] = each['nickname']
            item['imageLink'] = each['vertical_src']

            yield item
        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

#parse() : 解析response，并返回Item或Requests（需指定回调函数）。Item传给Item pipline持久化 ，
# 而Requests交由Scrapy下载，并由指定的回调函数处理（默认parse())，一直进行循环，直到处理完所有的数据为止。