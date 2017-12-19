# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ItcastPipeline(object):
    # 该方法可选，做初始化
    def __init__(self):
        self.filename = open('teachers.json', 'wb+')

    # 该方法必须的，做item数据处理工作
    def process_item(self, item, spider):
        json_text = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.filename.write(json_text.encode('utf-8'))
        return item

    # 该方法是可选的，调用结束的时候关闭文件
    def close_spider(self,spider):
        self.filename.close()
