import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from scrapy_crawlspider_06.items import ScrapyCrawlspider06Item


class ReadbookSpider(CrawlSpider):
    name = 'readbook'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1175_1.html']

    # rules = (
    #     Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
    # )

    # follow 是否跟进一直到爬完为止
    rules = (
        Rule(LinkExtractor(allow=r'/book/1175_\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print('读书网')
        img_list = response.xpath('//div[@class="bookslist"]/ul/li//div[@class="book-info"]//img')
        for img in img_list:
            # print(img)
            img_src = img.xpath('./@data-original').extract_first()
            # if img_src:
            #     img_src = img.xpath('./@src').extract_first()
            book_name = img.xpath('./@alt').extract_first()
            book = ScrapyCrawlspider06Item(img_src=img_src, book_name=book_name)
            yield book
