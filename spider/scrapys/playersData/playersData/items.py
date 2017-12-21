# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PlayersItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()  #姓名
    day = scrapy.Field()   #比赛时间
    againstTeam = scrapy.Field() #对阵球队
    playTime = scrapy.Field()
    shoot = scrapy.Field()
    points = scrapy.Field()  #得分
    rebounds = scrapy.Field() #篮板
    assist = scrapy.Field()  #助攻

