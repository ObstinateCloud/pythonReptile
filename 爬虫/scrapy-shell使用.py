# scrapy shell 用于爬虫编程过程中调试
# scrapy shell www.baidu.com
# 安装 iPython 自动不全高亮显示更加友好
# 可以直接对返回对象进行操作
#response.url
#response.text

#In [4]: response.xpath('//input[@id="su"]/@value')
#Out[4]: [<Selector xpath='//input[@id="su"]/@value' data='百度一下'>]
# In [5]: a = response.xpath('//input[@id="su"]/@value')
# In [6]: a.extract_first()
# Out[6]: '百度一下'



