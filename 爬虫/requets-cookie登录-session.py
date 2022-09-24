# 访问古诗文网站 模拟用户登录
import requests

demo_data = {
    '__VIEWSTATE': 'J0uw7V8Ny05IbLXImQxDjGH6fmpOrO6Fygrp5sFMn0mHoPG3gg/GF54RWj/kcQEkpQDghZSLi77l42+9zJgQ9yf1B/GC9EpPIRAFusXRiPtMcdfKm+7OATTCl5sgVyhJIrK2mHhjjW6dd/XlHYsE+vmwPic=',
    '__VIEWSTATEGENERATOR': 'C93BE1AE',
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13651128184@163.com',
    'pwd': 'zjyzjy520',
    'code': 'aaa',
    'denglu': '登录',
}

# data此处需要注意
#  '__VIEWSTATE'  '__VIEWSTATEGENERATOR' 为动态数据，为隐藏在页面中的元素生成

# 获取网页源码
login_page_url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
login_page_headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',

}
response = requests.get(url=login_page_url, headers=login_page_headers)

content = response.text

# with open('login.html', 'w', encoding='utf-8') as fp:
#     fp.write(content)

# 解析页面源码
from bs4 import BeautifulSoup
soup = BeautifulSoup(content,'lxml')
# 获取 __VIEWSTATE
view_state = soup.select('#__VIEWSTATE')[0].attrs.get('value')
print(view_state)
# 获取 __VIEWSTATEGENERATOR
view_state_generator = soup.select('#__VIEWSTATEGENERATOR')[0].attrs.get('value')
print(view_state_generator)
# 获取验证码地址
img_code = soup.select('#imgCode')[0].attrs.get('src')
print(img_code)
code_url = 'https://so.gushiwen.cn/RandCode.ashx'

import urllib.request
# 下载验证码到本地 不能使用文件下载此时请求的验证码，和下面的登录请求不是一个请求
# urllib.request.urlretrieve(url=code_url,filename='img_code.jpg')
session = requests.session()
response_code =session.get(code_url)
# 注意此时要使用二进制数据 因为我们要是用的是图片的下载
content_code = response_code.content
# wb模式 将二进制数据写入文件 此处图片加载有点儿慢需要手动刷新一下
with open('yanzhengma.jpg','wb') as fp:
    fp.write(content_code)

# 手动输入验证码
code_name = input('请输入验证码')

# 点击登录
post_data = {
    '__VIEWSTATE': view_state,
    '__VIEWSTATEGENERATOR': view_state_generator,
    'from': 'http://so.gushiwen.cn/user/collect.aspx',
    'email': '13651128184@163.com',
    'pwd': 'zjyzjy520',
    'code': code_name,
    'denglu': '登录',
}
# 登录地址
login_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'

login_resp = session.post(url=login_url,headers=login_page_headers,data=post_data)

content_post  = login_resp.text

with open('古诗文.html','w',encoding='utf-8') as fp:
    fp.write(content_post)