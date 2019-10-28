# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request


class MeinvPipeline(object):

    def __init__(self):
        self.path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            print('文件已存在')


    def process_item(self, item, spider):
        headline = item['headline']
        urls = item['urls']
        headline_path = os.path.join(self.path, headline)
        if not os.path.exists(headline_path):
            os.mkdir(headline_path)
        else:
            print('文件已存在')
        for i in urls:
            img_name = i.split('/')[-1]
            request.urlretrieve(i, os.path.join(headline_path, img_name))

        return item
