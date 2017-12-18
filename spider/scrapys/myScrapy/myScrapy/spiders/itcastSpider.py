# -*- coding: UTF-8 -*-
import scrapy

class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['http://www.itcast.cn/']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']

    def parse(self, response):
        with open('teachers.html', 'w+') as f:
            f.write(response.body)