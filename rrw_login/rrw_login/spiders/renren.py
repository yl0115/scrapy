# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'http://www.renren.com/PLogin.do'
        data = {'email': '970138074@qq.com', 'password': 'pythonspider'}
        request = scrapy.FormRequest(url,formdata=data, callback=self.parse_page)
        yield request
        pass

    def parse_page(self, response):
        with open('renren.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
