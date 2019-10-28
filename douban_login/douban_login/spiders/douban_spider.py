# -*- coding: utf-8 -*-
import scrapy


class DoubanSpiderSpider(scrapy.Spider):
    name = 'douban_spider'
    allowed_domains = ['douban.com']
    start_urls = ['https://accounts.douban.com/passport/login']

    def parse(self, response):
        url = r'https://accounts.douban.com/passport/login'
        pass




