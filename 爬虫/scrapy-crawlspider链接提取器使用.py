# CrawlSpider 将符合规则的链接提取出来

# 读书网
base_url = 'https://www.dushu.com/book/1175.html'

# CrawlSpider位于
from scrapy.linkextractors import LinkExtractor

# allow 正则表达式
link = LinkExtractor(allow=r'/book/1175_\d+\.html')

link.extract_links()