import urllib.request

# url = 'https://m.py.cn/jishu/jichu/18596.html'
# response = urllib.request.urlopen(url)
# 一个字节一个字节的读 方法1
# content = response.read().decode('utf-8')
# 返回n个字节
# content = response.read(10).decode('utf-8')
# 读取一行  方法2
# content = response.readline().decode('utf-8')
# 一行一行读  方法3
# content = response.readlines()

# print(content)
#  方法4
# print(response.getheaders())
#  方法5
# print(response.geturl())
#  方法6
# print(response.getcode())
# 一个类型 http.client.HTTPResponse
# print(type(response))

# 下载网页
# webPage = 'http://www.bjzalaw.com/pc_lh/xingshianjian.html#ZBDXSGF-178-PC#?&bd_vid=10312005369364703713'
# urllib.request.urlretrieve(webPage, 'test.html')

# 下载图片
# picUrl = 'https://t7.baidu.com/it/u=1595072465,3644073269&fm=193&f=GIF'
# urllib.request.urlretrieve(picUrl, 'test.jpg')

# 下载视频
# videoUrl = 'https://vd3.bdstatic.com/mda-mfuf163rfmkn36i7/sc/cae_h264_nowatermark/1624963807340099361/mda-mfuf163rfmkn36i7.mp4?v_from_s=hkapp-haokan-hbe&auth_key=1661955654-0-0-617630ba65405d483013041888324bd2&bcevod_channel=searchbox_feed&pd=1&cd=0&pt=3&logid=3054510386&vid=10554454971571011271&abtest=&klogid=3054510386'
# urllib.request.urlretrieve(videoUrl, 'test.mp4')

# url 的组成
#   协议          主机              端口
# http/https    www.baidu.com     80/443
#


right_url = 'http://www.baidu.com/'
# 此处有ua反扒
error_url = 'https://www.baidu.com/'
# UA 伪造
# 请求对象定制
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}
data = {}
# 关键字传参
# request = urllib.request.Request(url=error_url,headers=headers)
# request = urllib.request.Request(error_url,data,headers)
# response = urllib.request.urlopen(request)
# content = response.read().decode('utf-8')
# print(content)

# get请求 对参数转换为utf-8编码
unicode_str = urllib.parse.quote('张健云')
print(unicode_str)
