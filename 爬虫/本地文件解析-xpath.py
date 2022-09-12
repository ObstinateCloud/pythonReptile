# 浏览器安装扩展程序 xpath helper 使用ctrl+shift+x打开小黑框

# 安装lxml库 在python.exe 的位置 pycharm设置>interceptor 查看 C:\Users\zjy\venv\Scripts
# pip install lxml -i https://pypi.douban.com/simple --trusted-host pypi.douban.com
#  验证
from lxml import etree
# xpath 解析
# 解析 1.本地文件 .parse()
tree = etree.parse('xpath本地测试文件.html')
# 语法1 查找ul 下面的li   //所有下级  /直接下级 text()获取文本内容
# li_list = tree.xpath('//body/div/ul/li/text()') #写法1
# li_list = tree.xpath('//body//ul/li/text()') #写法2
# print(li_list)
# print(len(li_list))

# 语法2 谓词查询  找到所有id为l1的li
# li_l1 = tree.xpath('//ul/li[@id="l1"]/text()')
# print(li_l1)
# 语法2 谓词查询  找到所有class为c1的li
# li_c1 = tree.xpath('//ul/li[@class="c1"]/text()')
# print(li_c1)
# 语法3 属性查询  获取id为l1的li的class值
# li_class = tree.xpath('//ul/li[@id="l1"]/@class')
# print(li_class)

# 语法4 模糊查询  获取id为包含l的li
# li_contains = tree.xpath('//ul/li[contains(@id,"l")]/text()')
# print(li_contains)

# 语法5 模糊查询  获取id以c开头的li
# li_starts_with = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
# print(li_starts_with)
# li_starts_with = tree.xpath('//ul/li[starts-with(@class,"c")]/text()')
# print(li_starts_with)

# 语法6 逻辑运算  同时满足id包含l,并且class以c开头 and不能跨标签
# li_and = tree.xpath('//ul/li[@id="l1" and @class="c22"]/text()')
# print(li_and)

# 语法6 逻辑运算 或  满足id包含l,或class以c开头
li_or = tree.xpath('//ul/li[contains(@id,"l")]/text() | //ul/li[starts-with(@class,"c")]/text()')
print(li_or)
# print(tree)


# 解析 2.网络文件
