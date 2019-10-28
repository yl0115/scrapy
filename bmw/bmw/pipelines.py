# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib import request
from scrapy.pipelines.images import ImagesPipeline
from bmw import settings


class BmwPipeline(object):

    # def __init__(self):
    #     self.path = os.path.join(str(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'images')
    #     if not os.path.exists(self.path):
    #         os.mkdir(self.path)
    #     else:
    #         print('文件已经存在！')
    #
    # def process_item(self, item, spider):
    #     category = item['category']
    #     urls = item['urls']
    #     category_path = os.path.join(self.path, category)
    #     if not os.path.exists(category_path):
    #         os.mkdir(category_path)
    #     for i in urls:
    #         # 图片名称
    #         image_name = i.split('_')[-1]
    #         request.urlretrieve(i, os.path.join(category_path, image_name))
    #
    #     return item
    pass


class BMWImagesPipline(ImagesPipeline):

    def get_media_requests(self, item, info):
        """
        这个方法是在发送下载请求之前调用
        其实这个方法本身就是发送下载请求的
        :param item:
        :param info:
        :return:
        """
        request_objs = super(BMWImagesPipline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item
            return request_obj

    def file_path(self, request, response=None, info=None):
        """
        这个方法是在图片将要被存储的时候调用，来获取这个图片存储的路径
        :param request:
        :param response:
        :param info:
        :return:
        """
        path = super(BMWImagesPipline, self).file_path(request, response, info)
        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)

        return image_path

    


