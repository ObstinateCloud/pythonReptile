import scrapy
from scrapy_dangdang_04.items import ScrapyDangdang04Item


class DangdangSpider(scrapy.Spider):
    name = 'dangdang'
    allowed_domains = ['bang.dangdang.com']
    start_urls = ['http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-1']

    base_url = 'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent30-0-0-1-'
    page = 1

    def parse(self, response):
        print('当当网')
        # content = response.text
        # print(content)
        # 1. 在items中 自定义数据结构
        # 获取每个属性的xpath路径
        # //ul/li/div[@class="pic"]/a/img/@src
        # //ul/li/div[@class="name"]/a/@title
        # //ul/li/div[@class="price"]/p/span[@class="price_n"]/text()
        # 提取公共路径
        base_path = '//ul[@class="bang_list clearfix bang_list_mode"]/li'
        li_list = response.xpath(base_path)
        # selector 对象可以使用xpath再次解析
        # print(li_list)
        for li in li_list:
            img_src = li.xpath('./div[@class="pic"]/a/img/@src').extract_first()
            name = li.xpath('./div[@class="name"]/a/@title').extract_first()
            price = li.xpath('./div[@class="price"]/p/span[@class="price_n"]/text()').extract_first()
            # print(name, price, img_src)
            book = ScrapyDangdang04Item(img_src=img_src, name=name, price=price)
            # 2.使用piplines下载
            # 将book对象交给管道
            yield book
        # 一次请求处理完后
        if self.page < 4:
            self.page = self.page + 1
            url = self.base_url + str(self.page)
            yield scrapy.Request(url=url, callback=self.parse)

        pass
