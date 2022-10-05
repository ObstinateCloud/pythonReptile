import json

import scrapy


class FanyiSpider(scrapy.Spider):
    name = 'fanyi'
    allowed_domains = ['fanyi.baidu.com']

    # start_urls 直接访问post请求会报错
    # start_urls = ['http://fanyi.baidu.com/']
    #
    # def parse(self, response):
    #     pass

    def start_requests(self):
        url = 'https://fanyi.baidu.com/sug'
        data = {
            'kw': 'legend'
        }
        yield scrapy.FormRequest(url=url, formdata=data, callback=self.parse_second)

    def parse_second(self, response):
        content = response.text
        print(content)
        obj = json.loads(content)
        print(obj)
