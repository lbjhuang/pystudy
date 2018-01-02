# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os

class DouyuPipeline(ImagesPipeline):    #ImagesPipeline类，实现以下两个方法就可以下载图片了
    # def process_item(self, item, spider):
    #     return item
    #获取settings文件里的自定义的变量
    IMAGE_STORE = get_project_settings().get('IMAGES_STORE')

    def get_media_requests(self, item, info):
        imageUrl = item['imageLink']
        yield scrapy.Request(imageUrl)

    def item_complete(self, result, item, info):
        imagePath = [x['path'] for ok, x in result if ok]

        os.rename(self.IMAGES_STORE + "/" + imagePath[0], self.IMAGES_STORE + "/" + item["nickname"] + ".jpg")  #重命名文件
        item["imagePath"] = self.IMAGES_STORE + "/" + item["nickname"]

        return item
