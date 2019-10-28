# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline
import os
from huaban import settings


# class HuabanPipeline(object):
#     def process_item(self, item, spider):
#         return item


class HuabanImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        request_objs =super(HuabanImagePipeline, self).get_media_requests(item, info)
        for request_obj in request_objs:
            request_obj.item = item

        return request_objs

    def file_path(self, request, response=None, info=None):

        path = super(HuabanImagePipeline, self).file_path(request, response, info)
        category = request.item.get('category')
        images_store = settings.IMAGES_STORE
        category_path = os.path.join(images_store, category)
        if not os.path.exists(category_path):
            os.mkdir(category_path)
        image_name = path.replace('full/', '')
        image_path = os.path.join(category_path, image_name)

        return image_path

