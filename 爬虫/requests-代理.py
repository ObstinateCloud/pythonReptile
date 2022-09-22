import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    # 'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'BIDUPSID=5F6461D31E13768F18198C624CDB1AAC; PSTM=1632534269; __yjs_duid=1_5dc9994f67c1f8c8fe812cdbc9de28761633949720860; sug=3; ORIGIN=0; bdime=0; BDUSS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BDUSS_BFESS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BAIDUID=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; BD_UPN=12314753; MCITY=-131%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; BD_HOME=1; BA_HECTOR=2la4810hag2l2kah25akd4nv1hiom8r18; ZFY=TPceIGlTqJL9NLjYkSBcBXXzBqs0Bm20aT0KIS74SeY:C; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=37154_36544_37356_37139_36884_34813_37402_36805_37404_36789_37243_37260_26350_37447_22159; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; sugstore=1; H_PS_645EC=4cfdM9TGJBq%2FS9ewXiwDtPBv5QNPgd%2BgzD84CsfbtNFqJsiLB1a03I6vqKLUzAmbRVWb; COOKIE_SESSION=79268_0_8_9_7_8_1_0_8_6_0_4_79240_0_6_0_1663850801_0_1663850795%7C9%23930290_60_1662877547%7C9',
    'Host': 'www.baidu.com',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

data = {
    'wd': 'ip'
}
# https无法正常被代理
base_url = 'http://www.baidu.com/s?'
# 设置代理 https://proxy.seofangfa.com/
proxy = {
    'http':'120.26.37.240:8000'
}

response = requests.get(url=base_url, params=data, headers=headers,proxies=proxy)
response.encoding = 'utf-8'
# print(response.text)

with open('ip查询.html', 'w', encoding='utf-8') as fp:
    fp.write(response.text)
