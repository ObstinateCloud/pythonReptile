import urllib.request
import urllib.parse
import json

# 封装请求
def create_request(page):
    base_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
    }

    data = {
        'cname': '北京',
        'pid': '',
        'pageIndex': page,
        'pageSize': '10',
    }
    # post必须加 .encode('utf-8')
    data = urllib.parse.urlencode(data).encode('utf-8')

    request = urllib.request.Request(url=base_url, headers=headers,data=data)
    return request


# 获取内容
def getContent(request):
    response = urllib.request.urlopen(request)

    content = response.read().decode('utf-8')


    return content


# 下载到文件
def download(page, content):
    with open('kfc' + str(page) + '.json', 'w', encoding='utf-8') as fp:
        fp.write(content)


# 程序入口
if __name__ == '__main__':
    start_page = int(input('请输入开始页码:'))
    end_page = int(input('请输入结束页码:'))

    for i in range(start_page, end_page + 1):
        req = create_request(i)
        content = getContent(req)
        download(i, content)
