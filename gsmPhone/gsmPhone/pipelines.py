# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import datetime
import json

from itemadapter import ItemAdapter


class GsmphonePipeline:
    def process_item(self, item, spider):
        load_dict = []
        with open('labels.json', 'r', encoding='utf-8') as f:
            load_dict = json.load(f)
        # 将新传入的dict对象追加至list中
        load_dict.append(dict(item))
        # 将追加的内容与原有内容写回（覆盖）原文件
        with open('labels.json', 'w', encoding='utf-8') as f2:
            json.dump(load_dict, f2, ensure_ascii=False)
        return item
