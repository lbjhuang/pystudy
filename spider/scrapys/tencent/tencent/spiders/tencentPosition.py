# -*- coding: utf-8 -*-
import scrapy
from tencent.items import TencentItem


class TencentPositionSpider(scrapy.Spider):
    name = "tencent"
    allowed_domains = ["tencent.com"]
    url = "http://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [url + str(offset)]  # 初始化页面

    # 必须的函数，处理请求结果
    def parse(self, response):
        for each in response.xpath("//tr[@class='even'] | //tr[@class='odd']"):
            item = TencentItem()
            item['positionName'] = '没填写' if len(each.xpath('./td[1]/a/text()').extract()) == 0 else  each.xpath('./td[1]/a/text()').extract()[0]
            item['positionLink'] = '没填写' if len(each.xpath('./td[1]/a/@href').extract())  == 0 else each.xpath('./td[1]/a/@href').extract()[0]
            item['positionType'] = '没填写' if len(each.xpath('./td[2]/text()').extract())   == 0 else each.xpath('./td[2]/text()').extract()[0]
            item['positionNum']  = '没填写' if len(each.xpath('./td[3]/text()').extract())   == 0 else each.xpath('./td[3]/text()').extract()[0]
            item['workLocation'] = '没填写' if len(each.xpath('./td[4]/text()').extract())   == 0 else each.xpath('./td[4]/text()').extract()[0]
            item['publishTime']  = '没填写' if len(each.xpath('./td[5]/text()').extract())   == 0 else each.xpath('./td[5]/text()').extract()[0]

            # 将数据交给管道文件处理
            yield item

        # 处理完本页后再执行下一个
        if (self.offset < 2680):
            self.offset += 10  # 下一个页面参数
        else:
            raise ("结束啦")
        url = self.url + str(self.offset)  # 下一个页面的url拼接
        # Requst将请求重新发送给调度器去入队列，出队列，交给下载器下载，并设置回调到parse继续处理
        yield scrapy.Request(url, callback=self.parse)  # 如果请求地址是重复的，scrapy则不会再去发请求，所以上面的else也可以不用写了
