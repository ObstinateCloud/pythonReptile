# selenium是一个用于web应用程序测试的工具，直接在浏览器端运行，模拟用户操作 支持通过驱动模拟各种浏览器内核 如Chrome IE 火狐
import urllib.request
from urllib import request
# 爬取京东首页
url = 'https://www.jd.com'

# resp = urllib.request.urlopen(url)
#
# content = resp.read().decode('utf-8')
#
# print(content)
# 此时发现并没有返回 京东秒杀部分的内容， 因为服务器识别这个请求不是真正的浏览器发出的请求

# 需要使用selenium 模拟真实浏览器
# 1.驱动下载地址 https://chromedriver.storage.googleapis.com/index.html
# 2.下载完成后放到项目目录下
# 3. 安装selenium :pip install selenium
# 4. 导入selenium
from selenium import webdriver
# 5.创建浏览器操作对象 选择刚才下载的驱动
path = 'chromedriver.exe'

browser = webdriver.Chrome(path)

# 6.访问网站
browser.get(url)

# 7.获取网页源码
content = browser.page_source
print(content)

