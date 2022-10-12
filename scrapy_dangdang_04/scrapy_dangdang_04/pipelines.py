# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


# 使用前先在settings中开启管道 ITEM_PIPELINES
class ScrapyDangdang04Pipeline:
    # 前置方法 见官方文档
    def open_spider(self, spider):
        print('++++++++++++')
        self.fp = open('dangdang.json', 'w', encoding='utf-8')

    # item就是yield后面的对象
    def process_item(self, item, spider):
        # a 追加模式
        # 这种模式会频繁打开文件 推荐使用前后置方法
        # with open('dangdang.json','a',encoding='utf-8') as fp:
        #     # fp.write 只能写入字符串
        #     fp.write(str(item))
        self.fp.write(str(item))
        return item

    # 后置方法
    def close_spider(self, splider):
        print('-----------')
        self.fp.close()


# 多条管道下载共两步：框架会自动调用

# 1.定义管道类
# 2.在配置文件中开启管道
import urllib
class DangDangDownloadPipeline:
    def process_item(self, item, spider):
        img_src = item.get('img_src')
        file_name = './books/' + item.get('name') + '.jpg'
        urllib.request.urlretrieve(url=img_src, filename=file_name)
        return item
