import scrapy


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['bj.58.com']
    start_urls = ['https://bj.58.com/sou/?key=%E4%BF%9D%E5%A7%86']

    def parse(self, response):
        print('58保姆')
        pass
