# selenium是一个用于web应用程序测试的工具，直接在浏览器端运行，模拟用户操作 支持通过驱动模拟各种浏览器内核 如Chrome IE 火狐
from selenium import webdriver
from selenium.webdriver.common.by import By

# 模拟用户访问百度，搜索周杰伦
# 创建浏览器对象
# path = 'chromedriver'
# browser = webdriver.Chrome(path)
browser = webdriver.Chrome()
# 打开百度
url = 'https://www.baidu.com'
browser.get(url)

# 根据id找到百度一下按钮
button =browser.find_element(by=By.ID,value='su')
# print(button)
# 根据id找到输入框对象
# input = browser.find_element(by=By.ID,value='kw')
input = browser.find_element(by=By.NAME,value='wd')
# print(input)

link = browser.find_element(by=By.LINK_TEXT,value='hao123')


# 获取元素信息
btn_class = button.get_attribute('class')
# print(btn_class)
# 获取<>中的内容</>
# print(button.text)
# print(button.tag_name)
# print(link.text)

# 交互操作
# 输入周杰伦
input.send_keys('周杰伦')
# 点击百度一下
button.click()
# 滑到底部 执行js代码
js_bottom = 'document.documentElement.scrollTop=100000'
browser.execute_script(js_bottom)

import time
time.sleep(2)

# 点击下一页
next = browser.find_element(by=By.CLASS_NAME,value='n')
next.click()

# 返回上一页
browser.back()