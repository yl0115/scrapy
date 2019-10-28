# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from huaban.items import HuabanItem


class HuabanSpiderSpider(CrawlSpider):
    name = 'huaban_spider'
    allowed_domains = ['huaban.com']
    start_urls = ['http://huaban.com/']

    rules = (
        Rule(LinkExtractor(allow=r'https://huaban.com/pins/\d'), callback='parse_item', follow=False),
    )

    def parse_item(self, response):
        category = response.xpath('//div[@id="pin_view_layer"]/div[@class="pin-view"]//div[@class="side-part"]//div[@class="board-info"]/a/text()').get()
        image_urls = response.xpath('//div[@id="baidu_image_holder"]/img/@src').getall()


        item = HuabanItem()

