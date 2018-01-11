# -*- coding: UTF-8 -*-
import scrapy
from myScrapy.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 爬虫名字
    allowed_domains = ['http://www.itcast.cn/']  # 作用域
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#apython']  # 爬取地址

    def parse(self, response):
        teacher_list = response.xpath('//div[@class="li_txt"]')
        for each in teacher_list:
            item = ItcastItem()  # 实例化一个ItcastItem对象，对象包含items.py文件里的字段
            # 通过scrapy自带xpath匹配出所有根节点列表集合
            # extract() 用于将匹配的结果转换成unicode字符串或者列表
            name = each.xpath('./h3/text()').extract()
            title = each.xpath('./h4/text()').extract()
            desc = each.xpath('./p/text()').extract()
            # 赋值三个字段
            item['name'] = name[0]
            item['title'] = title[0]
            item['desc'] = desc[0]

            yield item   #yield 到管道文件来做数据处理
