import scrapy


class TongchengSpider(scrapy.Spider):
    name = 'tongcheng'
    allowed_domains = ['bj.58.com']
    start_urls = ['https://bj.58.com/sou/?key=%E4%BF%9D%E5%A7%86']

    def parse(self, response):
        print('58保姆')
        # 返回字符串
        content = response.text
        # 返回二进制数据
        biz_content = response.body
        print(content)
        # 获取按钮 自带xpath
        all_button = response.xpath('//div[@class="tabs"]')
        print('============')
        print(all_button)
        # 提取selector对象的data属性值
        #response.extract()
        #response.extract_first()
        pass
