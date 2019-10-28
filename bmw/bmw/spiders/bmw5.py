# -*- coding: utf-8 -*-
import scrapy
from bmw.items import BmwItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class Bmw5Spider(CrawlSpider):
    name = 'bmw5'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/pic/series/65.html']
    rules = (
        Rule(LinkExtractor(allow=r'https://car.autohome.com.cn/pic/series/65.+'), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        category = response.xpath('//div[@class="uibox"]/div/text()').get()
        srcs = response.xpath('//div[contains(@class,"uibox-con")]/ul/li/a/img/@src').getall()
        # srcs = list(map(lambda x:x.replace('240x180_0_q95_c42_', ''), srcs))
        # urls = []
        # for src in srcs:
        #     url = response.urljoin(src)
        #     urls.append(url)
        # srcs = list(map(lambda x:response.urljoin(x), srcs))
        srcs = list(map(lambda x:response.urljoin(x.replace('240x180_0_q95_c42_', '')), srcs))
        yield BmwItem(category=category, image_urls=srcs)
