# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import signals

class SinaguidePipeline(object):
    def process_item(self, item, spider):
        sonUrl = item['sonUrl']
        #文件名为子链接url中间部分(去掉http://和.shtml)，并将/替换成_，保存为.txt格式
        # 文件名为子链接url中间部分，并将 / 替换为 _，保存为 .txt格式
        filename = sonUrl[7:-6].replace('/', '_')
        filename += ".txt"

        fp = open(item['subFilename'] + '/' + filename, 'w')
        fp.write(item['content'])
        fp.close()

        return item
