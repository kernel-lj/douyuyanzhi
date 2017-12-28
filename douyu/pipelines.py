# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy
import os

# from settings import IMAGES_STORE as image_store

# class DouyuPipeline(ImagesPipeline):
#     image_save = get_project_settings().get("IMAGE_SAVE")
#     print "9999999999999999998888888888888"
#
#     def get_media_requests(self, item, info):
#         image_url = item["imageLink"]
#         yield scrapy.Request(image_url)
#
#     def item_completed(self, result, item, info):
#         image_path = [x["path"] for ok, x in result if ok]
#         os.rename(self.image_save + "/" + image_path[0], self.image_save + "/" + item["nickname"] + ".jpg")
#         item["imagePath"] = self.image_save + "/" + item["nickname"]
#         return item
    # def process_item(self, item, spider):
    #     return item

class DouyuPipeline(ImagesPipeline):
    image_save = get_project_settings().get("IMAGES_STORE")

    def get_media_requests(self, item, info):
        image_url = item["imageLink"]
        # print scrapy.Request(image_url)
        # print "*" * 40
        yield scrapy.Request(image_url)

    def item_completed(self, result, item, info):
        image_path = [x["path"] for ok, x in result if ok]
        os.rename(self.image_save + "/" + image_path[0], self.image_save + "/" + item["nickname"] + ".jpg")
        item["imagePath"] = self.image_save + "/" + item["nickname"]
        return item