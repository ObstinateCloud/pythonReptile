# 无界面浏览器 支持页面元素查找 js执行等 由于不进行css和gui渲染比真实的浏览器快 目前已经停更无法使用
from selenium import webdriver
path = 'phantomjs.exe'

browser = webdriver.PhantomJS(path)

url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu.png') #快照