# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .vars import *


class VbsbearPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        return item

class VbsbearMysqlPipeline(object):
    def process_item(self, item, spider):
        cursor.execute(sql, [item['name'], item['url'], item['key'], item['picture']])
        return item

    def close_spider(self, spider):
        conn.commit()
