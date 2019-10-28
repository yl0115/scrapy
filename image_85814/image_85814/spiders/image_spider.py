# -*- coding: utf-8 -*-
import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from image_85814.items import Image85814Item


class ImageSpiderSpider(CrawlSpider):
    name = 'image_spider'
    allowed_domains = ['85814.com']
    start_urls = ['https://www.85814.com/meinv/dachidumeinv/index_2.html']

    rules = (
        Rule(LinkExtractor(allow=r'https://www.85814.com/tu/.+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        category = response.xpath('//p[@id="o"]/i/a/text()').getall()
        category = category[-1]
        image_srcs =response.xpath('//dl[@id="d"]/dd/p/img/@src').getall()

        urls = []
        for src in image_srcs:
            # url = src+r'!800'
            # print(url)
            urls.append(src)
        yield Image85814Item(category=category, image_urls=urls)
