# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayersdataItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    game
    points = scrapy.Field()
    rebounds = scrapy.Field()
    assist = scrapy.Field()

