# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDangdang04Item(scrapy.Item):
    # define the fields for your item here like:
    # 名字
    name = scrapy.Field()
    # 图片
    img_src = scrapy.Field()
    # 价格
    price = scrapy.Field()
    pass
