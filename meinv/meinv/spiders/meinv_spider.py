# -*- coding: utf-8 -*-
import scrapy
from meinv.items import MeinvItem


class MeinvSpiderSpider(scrapy.Spider):
    name = 'meinv_spider'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/meitu.html']

    def parse(self, response):
        columns = response.xpath('//div[@class="list_cont list_cont2 w1180"]')
        for column in columns:
            classify = column.xpath('.//h2/text()').get()
            urls = column.xpath('.//ul[@class="clearfix"]/li/a/img/@data-original').getall()
            item = MeinvItem(headline=classify, urls=urls)
            yield item
