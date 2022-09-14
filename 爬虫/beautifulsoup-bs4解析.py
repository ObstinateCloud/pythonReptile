# BeautifulSoup-  简称bs4 和lxml类似的html解析器 缺点：效率比lxml低 优点：接口人性化使用简单
# 安装命令 pip install bs4
from bs4 import BeautifulSoup

# 创建soup对象 默认使用gbk编码  内核使用lxml
soup = BeautifulSoup(open('xpath本地测试文件.html',encoding='utf-8'),'lxml')

# print(soup)

# 根据标签查找数据
# 找到第一个符合条件的数据
# print(soup.ul)  # 返回整个标签内容
# print(soup.ul.attrs) # 返回标签属性

# bs4常用函数
##### find 返回第一个符合条件的数据
# print(soup.find('ul'))
# print(soup.find('ul',id='ul2'))
# class为关键字 加下划线处理
# print(soup.find('ul',class_='ul_class'))

##### find_all 返回所有符合条件的数据
# print(soup.findAll('ul'))
# 返回多个标签
# print(soup.findAll(['ul','ol']))
# 返回前几个数据
# print(soup.findAll('li',limit=6))

##### select 返回所有符合条件的数据列表
# print(soup.select('li'))
# 支持 类选择器
# print(soup.select('.ul_class'))
# 支持 id选择器
# print(soup.select('#ul1'))
# 支持 属性选择器
# print(soup.select('li[name]')) #有name属性的li
# print(soup.select('li[name="sh"]'))
# print(soup.select('li[class="c1"]'))

# 支持层级选择器
# 后代选择器
# print(soup.select('div li'))
# 子代选择器 *此处尽量加空格防止其他语言报错 bs4不会报错
# print(soup.select('div > ol > li'))
# 返回多种元素
# print(soup.select('ul,ol'))

# 获取节点内容
# 当标签中不包含其他标签时 string和get_text() 都可以获取到标签内容
# print(soup.select('li[class=c1]')[0].string)
# print(soup.select('li[class=c1]')[0].get_text())
# 当标签中包含其他标签时 只要有get_text() 可以获取到标签内容 ***目前都可以获取 此处留个疑问
# print(soup.select('li[class=c2]')[0].string)
# print(soup.select('li[class=c2]')[0].get_text())

# 获取标签名
print(soup.select('li[class=c1]')[0].name)

# 获取标签的属性值 三种方式
print(soup.select('li[class=c1]')[0].attrs.get('name'))
print(soup.select('li[class=c1]')[0].get('name'))
print(soup.select('li[class=c1]')[0]['name'])