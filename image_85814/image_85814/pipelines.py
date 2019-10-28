# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
from image_85814 import settings


# class Image85814Pipeline(object):
#     def process_item(self, item, spider):
#         return item


class TukuImagesPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        request_objs =super(TukuImagesPipeline, self).get_media_requests(item, info)
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
        path = super(TukuImagesPipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)

        return image_path
