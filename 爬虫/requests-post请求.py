import requests

base_url = 'https://fanyi.baidu.com/v2transapi?from=en&to=zh'

data = {
    'from': 'en',
    'to': 'zh',
    'query': 'legend',
    'transtype': 'translang',
    'simple_means_flag': '3',
    'sign': '788854.584263',
    'token': '9abfe1410f61c84acbc057d021c32291',
    'domain': 'common',
}

headers = {
    'Accept': '*/*',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Acs-Token': '1663838518492_1663856287475_+ULYdYGiyFjgGgEaHGmQwvm3Va2+WvHE9cplVMd3ZPotPByxYXkQLzgH5yrH5BLDovvzU2c11tK10+C8lTCz9L8CSpA6dBh+rcOCQn4Zxf+WdsIcTncCCyMKDpPCF8sJubL3zBxtEBITc0A7wmoMFOPFSXKlbR5ssGOfjPeoqf/P/7Q7vIZKtxrPyxRfkVI48c37Di1KJrRBr4tcH+xI4XFmWKyHtQL9frYk+uO8Jv/Qm5aBx1Nz7dY/MNUXhejTKua2Q0zTqrdX1qHIzGdR9msnUY+1ysK35FKa70MU+b/IyJa+SM7cvgvaswYH6+0iMiH+ql9k9Ct5vS00zy6aXA==',
    'Connection': 'keep-alive',
    'Content-Length': '137',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=5F6461D31E13768F18198C624CDB1AAC; PSTM=1632534269; __yjs_duid=1_5dc9994f67c1f8c8fe812cdbc9de28761633949720860; BDUSS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BDUSS_BFESS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; MCITY=-131%3A; APPGUIDE_10_0_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; BA_HECTOR=2la4810hag2l2kah25akd4nv1hiom8r18; ZFY=TPceIGlTqJL9NLjYkSBcBXXzBqs0Bm20aT0KIS74SeY:C; delPer=0; PSINO=1; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; H_PS_PSSID=37154_36544_37356_37139_36884_34813_37402_36805_37404_36789_37243_37260_26350_37447_22159; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1662040787,1662129608,1663856274; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1663856274; ab_sr=1.0.1_NzU3ZjdjMDhiNjYyYzA1YWZlY2E4MTdmZDFiNGRhYjMxYjRhNzlhZDcyM2I2NmU4OGUzYThkYTlkMDUxYzU2MGI2YmI2OWE1OTE4YjA5M2M1NGYwMzFhYjdiMGRkNjA5NzFmNzU5OWYzNDNlNWQ3NWM2MWE3ZGI3ZWZhMjIxYjljNjg3ZmI5MmZkOWZhZDI3MDc2NDdjMzU4NDlkOGFlNTc4YmIzMDYzMmIyM2ViZjE5NjlkOTliMmRjYjJkMmE0',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/?aldtype=16047',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}

# kwages 字典类型参数 可变长度
response = requests.post(url=base_url, data=data, headers=headers)

content = response.text
print(content)

import json

res = json.loads(content)
print(res)
