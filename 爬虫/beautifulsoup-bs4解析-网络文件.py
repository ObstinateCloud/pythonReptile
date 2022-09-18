# BeautifulSoup-  简称bs4 和lxml类似的html解析器 缺点：效率比lxml低 优点：接口人性化使用简单
import urllib.request
from urllib import request
# 星巴克菜单列表
url = 'https://www.starbucks.com.cn/menu/'

response = urllib.request.urlopen(url)

content = response.read().decode('utf-8')

# print(content)
# with open('星巴克.html','w',encoding='utf-8') as fp:
#     fp.write(content)

from bs4 import BeautifulSoup
soup = BeautifulSoup(content,'lxml')
# 获取所有产品名称
name_list = soup.select('ul[class="grid padded-3 product"] strong')

for name in name_list:
    print(name.get_text())