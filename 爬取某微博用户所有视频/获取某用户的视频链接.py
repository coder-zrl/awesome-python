import time
from selenium import webdriver
import re
driver = webdriver.Chrome()
req_url = "https://weibo.com/renminwang?is_all=1#_loginLayer_1591610993741"
# 开始请求
driver.get(req_url)
time.sleep(5)
data=driver.page_source
print(data)
url_name=re.findall('name=(\d{16}?) target',data)
for i in url_name:
    print(i)