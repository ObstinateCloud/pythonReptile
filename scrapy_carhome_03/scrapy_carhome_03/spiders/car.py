import scrapy


class CarSpider(scrapy.Spider):
    name = 'car'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = ['https://car.autohome.com.cn/price/brand-15.html']

    def parse(self, response):
        print('汽车之家')
        # content = response.text
        # print(content)
        name_list = response.xpath('//div[@class="main-title"]/a/text()')
        price_list = response.xpath('//span[@class="font-arial"]/text()')
        # for name in name_list:
        #     # 获取selector对象中的data属性
        #     print(name.extract())
        #
        # for price in price_list:
        #     # 获取selector对象中的data属性
        #     print(price.extract())

        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name,price)

        pass
