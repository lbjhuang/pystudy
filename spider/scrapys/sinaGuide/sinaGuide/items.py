# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
import sys


class SinaguideItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #大类的标题和url
    parentTitle = scrapy.Field()
    parentUrl = scrapy.Field()

    #小类标题和url
    subTitle = scrapy.Field()
    subUrl = scrapy.Field()

    #小类目录存放路径
    subFilename = scrapy.Field()
    #小类下面的子链接
    sonUrls = scrapy.Field()
    #文章标题和内容
    head = scrapy.Field()
    content = scrapy.Field()
