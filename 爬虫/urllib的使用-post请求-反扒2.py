import urllib.request

# 百度翻译案例 post
base_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'legend',
    'simple_means_flag': '3',
    'sign': '788854.584263',
    'token': '9abfe1410f61c84acbc057d021c32291',
    'domain': 'common',
}

# 反扒手段header伪造
header = {
    'Accept': '*/*',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1662102180431_1662130707124_3H+kXcoOOVcLWwoLCfdm6t13HW/YVVjJVm0PvAXNNozfQg9yfi3aZ5cdB9HiORY4mXj3TbQxNYrV4bgvrAKeAljNm8W9uypucj2fSD6oJpdSivFiVBwGunrM/AypAYEpAB6jQNhYRlOG9f8TnnOMS9tg/b5C8YQO7uOZyDzd9FIfuaA4SBI1EGDkCz7wApTBbDHKw5NaFkgfrIXaxMfqHrpXDShiR/0DKUE81dgjRgEOOPnz6x13X2K/93uWj69HPdhryxsyTd9nfZjugfLL0MxH0E1GlgwwCLN73RILqA49mQ/ZYaTgBDftSbMmlsyb',
    'Connection': 'keep-alive',
    'Content-Length': '118',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=5F6461D31E13768F18198C624CDB1AAC; PSTM=1632534269; __yjs_duid=1_5dc9994f67c1f8c8fe812cdbc9de28761633949720860; BDUSS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BDUSS_BFESS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; MCITY=-131%3A; BAIDUID_BFESS=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=fo3vneuorid&ss=l7ho459n&sl=n&tt=sin&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=nsx7&ul=st6b&hd=st8x"; APPGUIDE_10_0_2=1; H_PS_PSSID=37154_36544_36884_34813_36805_37243_37135_37260_26350_22159; BA_HECTOR=21a4al0hag8l80058g0mn2f91hh45e417; ZFY=TPceIGlTqJL9NLjYkSBcBXXzBqs0Bm20aT0KIS74SeY:C; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1662040787,1662129608; ab_sr=1.0.1_NmY0NDEyMjQ2Njg1ZDk1MjEyODdlYmVmMzJjM2NkMzNmYjU5ODlkNTE5NWVmYTgxYjVjODdmZGM5NTIyZjRlOWY1M2I0ZWM5YzNmNTdhY2ZiMGFkYWMwNTFlZmI5OWFmNWYyOWRhNTdkMzEyYjUyODlhNDg5NDAzYjQ5MmFlZDcyYzc1MTEzNGE5NmUxYmVmZDg2MWUxMDdjYzQ4MDE1ZTgxZDIzOGM4MmVlMDVjOTU2NTk3ZTcxY2ExY2QwMGFk; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1662130705',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
# post 请求参数必须编码 必须encode为字符型
data = urllib.parse.urlencode(data).encode('utf-8')
# 请求对象定制  此时不加header会报错
# request = urllib.request.Request(url=base_url, data=data)

request = urllib.request.Request(url=base_url, data=data, headers=header)

resp = urllib.request.urlopen(request)

print(resp)

content = resp.read().decode('utf-8')

print(content)

print(type(content))
# 需要将字符串转为json
import json

print(json.loads(content))
