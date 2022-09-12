#需求 下载站长素材网站伤感图片区十页的图片

# 第一页请求格式 https://sc.chinaz.com/tupian/shanggan.html
# 第二页请求格式 https://sc.chinaz.com/tupian/shanggan_2.html
base_url ='https://sc.chinaz.com/tupian/shanggan'
suffix = '.html'

# 请求html页面内容
import urllib.request
def get_html_content(url):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'cz_statistics_visitor=8f8d0a63-a825-bdaf-dfb9-8825f398498a; Hm_lvt_398913ed58c9e7dfe9695953fb7b6799=1662969197; Hm_lpvt_398913ed58c9e7dfe9695953fb7b6799=1662969360',
        'Host': 'sc.chinaz.com',
        'Referer': 'https://sc.chinaz.com/tupian/shanggan.html',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    }
    request = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content
# 下载图片
from lxml import etree
def download_img(content):
    html_treee = etree.HTML(content)
    # 获取图片名列表
    name_list = html_treee.xpath('//div[starts-with(@class,"tupian-list")]/div/img/@alt')
    # 获取图片地址列表 一般图片网站会使用懒加载  此时真正的图片地址在data-original
    src_list = html_treee.xpath('//div[starts-with(@class,"tupian-list")]/div/img/@data-original')
    #下载图片
    for i in range(len(name_list)):
        img_name = name_list[i]
        img_url = 'https:'+src_list[i]
        urllib.request.urlretrieve(url=img_url,filename='./站长图片/'+img_name+'.jpg')


if __name__ == '__main__':
    start = int(input('请输入起始页码:'))
    end = int(input('请输入结束页码:'))
    url = ''
    for page_i in range(start,end+1):
        if page_i==1:
            url = base_url+suffix
        else:
            url = base_url+'_'+str(page_i)+suffix
        content = get_html_content(url)
        download_img(content)


