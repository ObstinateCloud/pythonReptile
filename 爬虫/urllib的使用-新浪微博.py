import urllib.request

# 新浪微博案例 get
base_url = 'https://weibo.com/ajax/profile/info?uid=5203322066'

# 反扒手段header伪造
header = {
    'accept': 'application/json, text/plain, */*',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'client-version': 'v2.34.95',
    'cookie': 'XSRF-TOKEN=i02buHk3Fg9gcL58lQKu_GSk; PC_TOKEN=ae289a7dd3; login_sid_t=3a9cab62daf113396375a06b27c5be33; cross_origin_proto=SSL; WBStorage=4d96c54e|undefined; wb_view_log=1536*8641.25; _s_tentry=weibo.com; Apache=7457196626102.787.1662806508003; SINAGLOBAL=7457196626102.787.1662806508003; ULV=1662806508035:1:1:1:7457196626102.787.1662806508003:; ALF=1694342558; SSOLoginState=1662806558; SUB=_2A25OGBpODeRhGeNM61ES8izMzTqIHXVtbAyGrDV8PUNbmtANLWzukW9NTl6efVJ29wdHbeNvSgcSSKmeldAp8PZP; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5z3HN9Nu8z28GA6cZ2G_Ij5JpX5KzhUgL.Fo-Eehe0eoz7Soq2dJLoIXnLxKBLB.eL1KnLxK.L1-zL1h-LxKBLB.2LB.2LxKML1KBL1-qLxKqLB-BLBKeLxK-L1h5LB.eLxKML1K.LB-zLxKML12zL1hzt; WBPSESS=KG6OMaXegxEtuqqQoQW7QTBHLKwkYn6hqxyxKlXOHSKDIIi-_jVmjqe7IPVcMe7kuak5mxZtN5osOgpj8054I9GYvrW4FsT6TZfaAMZGjwXFDyz1jlAxFhtYSe3h6W1xtCmjXNBtewlmoMwJ87ABGQ==',
    'referer': 'https://weibo.com/u/5203322066',# 一般用于防盗链
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'server-version': 'v2022.09.08.2',
    'traceparent': '00-0cf4acd6c5016df890c0ee423855e38d-6f86588a8ddb13e4-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
    'x-xsrf-token': 'i02buHk3Fg9gcL58lQKu_GSk',
}

# 请求对象定制  此时不加header会报错
request = urllib.request.Request(url=base_url, headers=header)

response = urllib.request.urlopen(request)

# 未登录会跳转到登录页面，登录页面的编码为gb2312
# content = response.read().decode('gb2312')
# 登录会跳转到主页面，主页面的编码为utf-8
content = response.read().decode('utf-8')

print(content)

# with open('weibo_login.html', 'w', encoding='gb2312') as fp:
#     fp.write(content)

with open('weibo_main.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
