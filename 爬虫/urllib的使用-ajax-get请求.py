import urllib.request

# 单次请求
# url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action=&start=0&limit=10'
#
# # UA 伪造
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
# }
# data = {}
# # 请求对象定制
# # 关键字传参
# request = urllib.request.Request(url=url, headers=headers)
# # 获取响应数据
# response = urllib.request.urlopen(request)
#
# content = response.read().decode('utf-8')
# print(content)
#
# # 保存数据到文件  open默认为gbk
# fp = open('豆瓣.json','w',encoding='utf-8')
# fp.write(content)
# fp.close()


# 程序封装 请求前10页
import urllib.parse


# 封装请求
def create_request(page):
    base_url = 'https://movie.douban.com/j/chart/top_list?type=5&interval_id=100%3A90&action='

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    data = {
        'start': (page - 1) * 20,
        'limit': 20,
    }

    data = urllib.parse.urlencode(data)

    url = base_url + data

    # print(url)

    request = urllib.request.Request(url=url, headers=headers)
    return request


# 获取内容
def getContent(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')

    return content

# 下载到文件
def download(page,content):
    with open('douban_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)

# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入开始页码:'))
    end_page = int(input('请输入结束页码:'))

    for i in range(start_page, end_page + 1):
        req = create_request(i)
        content = getContent(req)
        download(i,content)
