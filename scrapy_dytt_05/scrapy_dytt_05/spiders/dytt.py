import scrapy

from scrapy_dytt_05.items import ScrapyDytt05Item


# 电影天堂 多级页面爬取

class DyttSpider(scrapy.Spider):
    name = 'dytt'
    allowed_domains = ['m.dytt8.net']
    start_urls = ['https://m.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):
        print('电影天堂')
        # 获取列表第一条记录的名字
        name = response.xpath('//div[@class="co_content8"]//table[1]//tr[2]/td[2]//a/text()').extract_first()
        href_url = response.xpath('//div[@class="co_content8"]//table[1]//tr[2]/td[2]//a/@href').extract_first()
        print(name)
        print(type(href_url))
        href_url = 'https://m.dytt8.net' + href_url
        print(href_url)
        # 访问href地址 用meta向下级页面传参
        yield scrapy.Request(url=href_url, meta={'name': name}, callback=self.second_step)  # 此处second_step不能传参数
        pass

    def second_step(self, response):
        print('second_step')
        # 获取封面图片地址
        img_src = response.xpath('//div[@id="Zoom"]//img/@src').extract_first()
        print(img_src)

        # 接受上级页面的传参 使用meta
        name = response.meta['name']
        movie = ScrapyDytt05Item(name=name,img_src=img_src)
        yield movie

