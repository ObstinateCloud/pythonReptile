import urllib.request

# 自定义handler处理器
base_url = 'http://www.baidu.com/s?wd=ip'

# 反扒手段header伪造
header = {
'Accept':'application/json, text/javascript, */*; q=0.01',
# 'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie':'BIDUPSID=5F6461D31E13768F18198C624CDB1AAC; PSTM=1632534269; __yjs_duid=1_5dc9994f67c1f8c8fe812cdbc9de28761633949720860; sug=3; ORIGIN=0; bdime=0; BDUSS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BDUSS_BFESS=U4yeUxJRVUzZEU3b2M4SjhLbm51SDJXQ3NhVXpHSWo3WHJPTjRoQTR2RGxCcnBoRVFBQUFBJCQAAAAAAAAAAAEAAADkLe9T08XRxcjLyfrV~fGyv~EAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAOV5kmHleZJhY; BAIDUID=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; BD_UPN=12314753; MCITY=-131%3A; ispeed_lsm=2; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=3EEF79FCC67E63A6A19648162F15A1B4:FG=1; BA_HECTOR=0l0185a12h818k852gag6rg21hhope019; ZFY=TPceIGlTqJL9NLjYkSBcBXXzBqs0Bm20aT0KIS74SeY:C; BD_HOME=1; delPer=0; BD_CK_SAM=1; PSINO=1; H_PS_PSSID=37154_36544_37356_36884_34813_36805_37243_37260_26350_37284_22159; COOKIE_SESSION=401628_2_8_9_9_21_0_0_8_6_0_6_199500_924547_0_6_1662475921_1662877553_1662877547%7C9%23930290_60_1662877547%7C9; shifen[209747595531_47916]=1662877551; BCLID=11758985975764098495; BCLID_BFESS=11758985975764098495; BDSFRCVID=7BuOJeC629VsKMnjXqjZb_2YRJN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; BDSFRCVID_BFESS=7BuOJeC629VsKMnjXqjZb_2YRJN1TM6TH6aoGj5RLCG2dC44-Pl4EG0P8f8g0KubJ2MRogKK0mOTHv8F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tJ4toCPMJI_3fP36q4Rh-tFO-frQaC62aKDs_hoaBhcqEIL4eqj5yUuHMR7DaqTaXbrkbqcktxbYMxbSj4QoQPT004vm05jb0bPJsxJsJp5nhMt9b67JDMP0-4CHWljy523ion6vQpn-bhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0-nDSHHDJJ6Dq3H; H_BDCLCKID_SF_BFESS=tJ4toCPMJI_3fP36q4Rh-tFO-frQaC62aKDs_hoaBhcqEIL4eqj5yUuHMR7DaqTaXbrkbqcktxbYMxbSj4QoQPT004vm05jb0bPJsxJsJp5nhMt9b67JDMP0-4CHWljy523ion6vQpn-bhQ3DRoWXPIqbN7P-p5Z5mAqKl0MLPbtbb0xb6_0-nDSHHDJJ6Dq3H; baikeVisitId=107b0c4f-ce2b-401c-a5b8-1cfbcff52d56; BDRCVFR[feWj1Vr5u3D]=mk3SLVN4HKm; sugstore=1; H_PS_645EC=4a0fiHy0dXtxxlvRC5KG9cX3OPXEBuDiKnw9fVNCebqvJPDuRZ%2F8ayErtruKT29ZgzbN',
'Host':'www.baidu.com',
'Referer':'https://www.baidu.com/s?wd=ip&rsv_spt=1&rsv_iqid=0x95e9a6230022c75e&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&rqlang=cn&tn=baiduhome_pg&rsv_enter=0&rsv_dl=tb&oq=ip&rsv_btype=t&rsv_t=71e8xkMSyAo9AKIgZzxZTkBCiCW%2FFFhOeavLLqdNJjoVmDXxs9H%2BdkFgE39cd0K64SLG&rsv_pq=a947c538000a07fd&prefixsug=ip&rsp=5',
'sec-ch-ua':'"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
'sec-ch-ua-mobile':'?0',
'sec-ch-ua-platform':'"Windows"',
'Sec-Fetch-Dest':'empty',
'Sec-Fetch-Mode':'cors',
'Sec-Fetch-Site':'same-origin',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }

# 请求对象定制  此时不加header会报错
request = urllib.request.Request(url=base_url, headers=header)
# handler 三步
# # 获取handler 对象
# handler = urllib.request.HTTPHandler()
# # 获取open对象
# opener = urllib.request.build_opener(handler)
# # 调用open方法
# response =  opener.open(request)

# 设置代理
proxy = {
    'http':'223.96.90.216:8085'
}
# # 优化代理池
# proxies_pool = [
#     {'http':'223.96.90.216:8085'},
#     {'http':'112.14.47.6:52024'},
#     {'http':'101.200.127.149:3129'},
# ]
# import random
#
# print(random.choice(proxies_pool))

handler = urllib.request.ProxyHandler(proxy)

opener = urllib.request.build_opener(handler)

response = opener.open(request)


content = response.read().decode('utf-8')

# print(content)

with open('ip查询.html','w',encoding='utf-8') as fp:
    fp.write(content)