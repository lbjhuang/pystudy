# -*- coding: utf-8 -*-
import scrapy
import os
import sys
from sinaGuide.items import SinaguideItem


class sinaGuide(scrapy.Spider):
    name = "sinaGuide"
    allowed_domains = ["sina.com.cn"]
    start_urls = ["http://news.sina.com.cn/guide/"]  # 初始化页面

    # 必须的函数，处理请求结果
    def parse(self, response):
        items = []
        #所有大类url，标题
        parentUrl = response.xpath("//div[@id='tab01']/div/h3/a/@href").extract()
        parenTitle = response.xpath("//div[@id='tab01']/div/h3/a/text()").extract()
        #所有小类url，标题
        subUrl = response.xpath("//div[@id='tab01']/div/ul/li/a/@href").extract()
        subTitle = response.xpath("//div[@id='tab01']/div/ul/li/a/text()").extract()

        #爬取所有大类
        for i in range(0, len(parenTitle)):
            #指定大类目录路径和目录名称, 无则新建该目录
            parentFilename = "./Data/" + parenTitle[i]
            if (not os.path.exists(parentFilename)):
                os.makedirs(parentFilename)

            #爬取所有小类
            for j in range(0, len(subUrl)):
                item = SinaguideItem()  #取得 items文件中的字段并赋值
                item['parentTitle'] = parenTitle[i]
                item['parentUrl'] = parentUrl[i]     #每个大类url格式: http://news.sina.com.cn/

                #检查小类url是否以同类别大类的url开头，是则是属于同一个大类
                if_belong = subUrl[j].startswith(item['parentUrl'])
                if (if_belong):
                    subFilename = parentFilename + '/' + subTitle[j]
                    #如果不存在则创建目录
                    if (not os.path.exists(subFilename)):
                        os.makedirs(subFilename)
                    #存储小类url,title,filename字段数据
                    item['subTitle'] = subTitle[j]
                    item['subUrl'] = subUrl[j]       #每个小类url格式: http://news.sina.com.cn/society
                    item['subFilename'] = parentUrl[i]

                    items.append(item)   #把所有的小类的添加到大列表里面
        # 发送每个小类url的Request请求，得到Response连同包含meta数据 一同交给回调函数 second_parse 方法处理
        for item in items:
            yield scrapy.Request(url = item['subUrl'], meta={'meta_1':item}, callback=self.second_parse)

    #对返回的小类url再进行递归请求
    def second_parse(self, response):
        #提取每次response的meta数据
        meta_1 = response.meta['meta_1']
        #取出小类里面所有子链接
        sonUrls = response.xpath('//a/@href').extract()
        items = []
        for i in range(0, len(sonUrls)):
            #检查每个链接是否以大类url开头，以.shtml结尾，是返回True
            if_belong = sonUrls[i].endswith('.shtml') and sonUrls[i].startswith(meta_1['parentUrl'])
            #如果属于本大类，获取字段值放在同一item进行下一步传输
            if (if_belong):
                item = SinaguideItem()
                item['parentTitle'] = meta_1['parentTitle']
                item['parentUrl'] = meta_1['parentUrl']
                item['subUrl'] = meta_1['subUrl']
                item['subTitle'] = meta_1['subTitle']
                item['subFilename'] = meta_1['subFilename']
                item['sonUrls'] = sonUrls[i]
                items.append(item)

                # 发送每个小类子链接的url的Request请求，得到Response连同包含meta数据 一同交给回调函数 detail_parse 方法处理得到想要的数据
            for item in items:
                yield scrapy.Request(url=item['sonUrl'], meta={'meta_2': item}, callback=self.detail_parse)


    # 数据解析方法，获取文章标题和内容
    def detail_parse(self, response):
        item = response.meta['meta_2']
        content = ""
        head = response.xpath("//h1[@id='main_title']/text()")
        content_list = response.xpath("//div[@id='article']/p/text()")

        #将p标签里面的文本内容合并到一起
        for content_one in content_list:
            content += content_one

        item['head'] = head
        item['content'] = content

        yield item