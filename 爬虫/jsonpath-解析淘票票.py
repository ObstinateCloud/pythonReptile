# 安装 jsonpath pip install jsonpath
import urllib.request

import jsonpath
import json

# 爬取 淘票票城市信息

base_url = 'https://dianying.taobao.com/cityAction.json?activityId&_ksTS=1663163326906_109&jsoncallback=jsonp110&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    # ':authority': 'dianying.taobao.com',
    # ':method': 'GET',
    # ':path': '/cityAction.json?activityId&_ksTS=1663163326906_109&jsoncallback=jsonp110&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    # ':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    # 'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'bx-v': '2.2.3',
    'cookie': 'cna=KFLZGfNwVVACAWeOjMlQydqX; t=fca674acdff88de709e2eded2a70b1a9; cookie2=1b7f4380467e4beade4cbd59a6b3754a; v=0; _tb_token_=3e36b143eb3de; xlly_s=1; l=eBS7kV-qLKnClYrUBO5anurza77OoQdbzsPzaNbMiInca691TF92_NCEcFuD7dtjgt5eGeKPNKfZAdewzA4U-FsWHpfuKtyuJtvHRe1..; tfstk=c_VCBwMNKHxCZZssbv_NY3EOEXcla0IsS9iLRG89ZI05D64oXsfDgmNcB8xia431.; isg=BJCQS6QYxzKdk5qVCN1wEyT0Yd7iWXSjbmuhrYpi3Ou-xTJvM2zhMhu7nY0lFSx7',
    'referer': 'https://dianying.taobao.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
from urllib import request
# 请求对象定制
request = urllib.request.Request(url=base_url,headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

# print(content)

# 解决jsonp 格式问题 去掉jsonp 标识
content = content.split('(')[1].split(')')[0]
print(content)

# jsonpath 只能识别本地文件
with open('淘票票.json','w',encoding='utf-8') as fp:
    fp.write(content)

obj = json.load(open('淘票票.json','r',encoding='utf-8'))

city_list = jsonpath.jsonpath(obj,'$..regionName')

print(len(city_list))



