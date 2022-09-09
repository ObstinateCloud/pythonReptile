import urllib.request

# 百度翻译案例 post
base_url = 'https://fanyi.baidu.com/sug'

data = {
    'kw': 'legend'
}
# post 请求参数必须编码 必须为字符型
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=base_url, data=data)

resp = urllib.request.urlopen(request)

print(resp)

content = resp.read().decode('utf-8')

print(content)

print(type(content))
# 需要将字符串转为json
import json

print(json.loads(content))
