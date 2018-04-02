# -*- coding: UTF-8 -*-
import scrapy
from jsssc.items import JssscItem


class JssscSpider(scrapy.Spider):
    name = 'jsssc'
    allowed_domains = ['131288.com']
    start_urls = ['http://131288.com/common/draw?gameOpen=53']

    def parse(self, response):
        for each in response.xpath("//tbody[@id='cqssc_draw_list_tbody']/tr"):
            item = JssscItem()

            #xpath解析
            item['openPeriod'] = each.xpath('./td/span[contains(@class, "text1")]//text()').extract()[0]
            item['openNumber'] = each.xpath('./td/span[contains(@class, "red_big")]//text()').extract()[0]
            print(item['openNumber'])

            yield item