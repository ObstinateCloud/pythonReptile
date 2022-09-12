# 浏览器安装扩展程序 xpath helper 使用ctrl+shift+x打开小黑框
import urllib.request

# 获取百度首页的百度一下文字
url = 'http://www.baidu.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
}

request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
# print(content)

#解析网页源码
from lxml import etree
html_tree = etree.HTML(content)
print(html_tree)
# 此处可以通过xpath helper工具校验表达式
result = html_tree.xpath('//input[@id="su"]/@value')
print(result)

