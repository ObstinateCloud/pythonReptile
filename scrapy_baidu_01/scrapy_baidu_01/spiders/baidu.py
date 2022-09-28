import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'baidu'
    # 允许访问的域名 下面不再允许访问京东等其他域名
    allowed_domains = ['www.baidu.com']
    # 起始访问的地址
    start_urls = ['http://www.baidu.com/']

    #
    def parse(self, response):
        # 注释settings文件中的 ROBOTSTXT_OBEY = False https://www.baidu.com/robots.txt 关闭君子协定
        print('hello 百度')
        pass
