# -*- coding: utf-8 -*-
import scrapy
from playersData.items import PlayersItem


class playerDataSpider(scrapy.Spider):
    name = "players"
    allowed_domains = ["nba.hupu.com/players/"]

    start_urls = [
        "https://nba.hupu.com/players/kyrieirving-3554.html",  #欧文
        "https://nba.hupu.com/players/kevinlove-3004.html",   #乐福
        "https://nba.hupu.com/players/lebronjames-650.html",  #詹姆斯
        "https://nba.hupu.com/players/anthonydavis-3638.html", #戴维斯
        "https://nba.hupu.com/players/deandrejordan-3014.html", #小乔丹
        "https://nba.hupu.com/players/spencerdinwiddie-4955.html", #丁威迪
        "https://nba.hupu.com/players/rondaehollisjefferson-150014.html",  #霍利斯杰弗森
        "https://nba.hupu.com/players/rickyrubio-3345.html", #卢比奥
        "https://nba.hupu.com/players/donovanmitchell-150510.html", #多诺万米切尔
        "https://nba.hupu.com/players/lonzoball-150429.html",  #郎佐鲍尔
        "https://nba.hupu.com/players/victoroladipo-4819.html", #奥拉迪波
        "https://nba.hupu.com/players/joelembiid-4958.html",  #恩比德
        "https://nba.hupu.com/players/jamesharden-3306.html",  #哈登
        "https://nba.hupu.com/players/bradleybeal-3640.html", #比尔
        "https://nba.hupu.com/players/johnwall-3449.html",  #沃尔
        "https://nba.hupu.com/players/michaelkiddgilchrist-3639.html", #麦基吉
        "https://nba.hupu.com/players/nicolasbatum-3025.html", #巴图姆
        "https://nba.hupu.com/players/russellwestbrook-3016.html", #威少
        "https://nba.hupu.com/players/carmeloanthony-252.html", #安东尼
        "https://nba.hupu.com/players/paulgeorge-3458.html", #乔治
        "https://nba.hupu.com/players/nikolavucevic-3569.html", #武切维奇
        "https://nba.hupu.com/players/jonathonsimmons-150073.html",#魔术西蒙斯
        "https://nba.hupu.com/players/ryananderson-3046.html",#火箭安德森
        "https://nba.hupu.com/players/jimmybutler-3583.html", #巴特勒
        "https://nba.hupu.com/players/karlanthonytowns-150037.html",#唐斯
    ]

    # 必须的函数，处理请求结果
    def parse(self, response):
        for each in response.xpath("//div[@class='team_hig'][1]//table[@class='players_table bott bgs_table']/tbody/tr[@class='color_font1 borders_btm'][position()>1]"):
            item = PlayersItem()
            item['name'] = response.xpath('//p[@class="bread-crumbs"]/b/text()').extract()[0]
            item['day'] = each.xpath('./td[1]/text()').extract()[0]
            item['againstTeam'] = each.xpath('./td[2]/text()').extract()[0]
            item['playTime']  = each.xpath('./td[4]/text()').extract()[0]
            item['shoot'] = each.xpath('./td[5]/text()').extract()[0]
            item['rebounds'] = each.xpath('./td[11]/text()').extract()[0]
            item['assist'] = each.xpath('./td[12]/text()').extract()[0]
            item['points']= each.xpath('./td[17]/text()').extract()[0]

            # 将数据交给管道文件处理
            yield item



