# -*- coding: utf-8 -*-
import scrapy
from bsbdj.items import BsbdjItem
from scrapy.http.response.html import HtmlResponse


class BudejieSpider(scrapy.Spider):
    name = 'budejie'
    allowed_domains = ['budejie.com']
    start_urls = ['http://www.budejie.com/1']
    base_domain = r'http://www.budejie.com/'

    def parse(self, response):
        text = response.xpath('//div[@class="j-r-list"]/ul/li')
        for i in text:
            author = i.xpath('.//a[@class="u-user-name"]/text()').get().strip()
            content = i.xpath('.//div[@class="j-r-list-c-desc"]/a/text()').get().strip()
            item = BsbdjItem(author=author, content=content)
            yield item
        page_num = response.xpath('//a[@class="pagenxt"]/@href').get()
        print('='*40)
        print(page_num)
        if int(page_num) == 51:
            return
        else:
            yield scrapy.Request(self.base_domain+page_num, callback=self.parse)
        print('='*40)



