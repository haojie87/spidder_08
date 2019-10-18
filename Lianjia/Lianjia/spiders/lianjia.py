# -*- coding: utf-8 -*-
import scrapy


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = ['http://bj.lianjia.com/']

    def parse(self, response):
        pass
