import urllib.request

# csdn案例 post
base_url = 'https://blog.csdn.net/m0_63722685/article/details/126393950'
error_base_url = 'https://blog.csdn.net/m0_63722685/article/details/12639395011'
error_base_url = 'https://www.lengedyun.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

try:
    request = urllib.request.Request(url=error_base_url, headers=headers)

    resp = urllib.request.urlopen(request)

    content = resp.read().decode('utf-8')

    print(content)
except urllib.error.HTTPError:
    print('系统正在升级....')
except urllib.error.URLError:
    print('请检查地址...')