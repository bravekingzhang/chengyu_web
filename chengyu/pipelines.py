# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json


class ChengyuPipeline(object):
    def process_item(self, item, spider):
        return item


# 格式化输出 Json (将每一个 item 都输出为一个 json 字符串)
class JsonWritePipeline(object):
    def __init__(self):
        self.output = open('json_format.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.output.write(line)
        return item

    def close_spider(self, spider):
        self.output.close()
