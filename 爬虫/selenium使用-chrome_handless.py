# chrome-handless模式 不需要打开浏览器就可以实现浏览器效果
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def chrome_handless_browser():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    path = r'C:\Users\zjy\AppData\Local\Google\Chrome\Application\chrome.exe'
    chrome_options.binary_location = path
    browser = webdriver.Chrome(options=chrome_options)
    return browser

browser = chrome_handless_browser();
url = 'https://www.baidu.com'
browser.get(url)
browser.save_screenshot('baidu_screenshot.png')