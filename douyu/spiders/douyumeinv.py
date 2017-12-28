# -*- coding: utf-8 -*-
import scrapy
import json
from douyu.items import DouyuItem

class DouyumeinvSpider(scrapy.Spider):
    name = 'douyumeinv'
    allowed_domains = ['capi.douyucdn.cn']

    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0
    start_urls = [url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)["data"]
        # 请求的数据为空的话退出请求: 第二种写法
        if not len(data_list):
            return

        for data in data_list:
            item = DouyuItem()
            item["nickname"] = data["nickname"]
            item["imageLink"] = data["vertical_src"]
            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)

        # 第一种写法
        # if self.offset <= 270:
        #     self.offset += 20
        # yield scrapy.Request(self.url + str(self.offset), callback=self.parse)
