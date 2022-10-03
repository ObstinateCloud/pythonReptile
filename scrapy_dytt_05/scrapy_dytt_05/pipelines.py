# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapyDytt05Pipeline:
    # 前置方法 见官方文档
    def open_spider(self, spider):
        print('++++++++++++')
        self.fp = open('movie.json', 'w', encoding='utf-8')


    def process_item(self, item, spider):
        self.fp.write(str(item))
        return item

        # 后置方法

    def close_spider(self, splider):
        print('-----------')
        self.fp.close()