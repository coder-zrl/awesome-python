from selenium import webdriver
from lxml import etree
browser = webdriver.Chrome()
url = "https://www.baidu.com"
# 开始请求
browser.get(url)
#得到页面源代码
response=browser.page_source   #字符串形式
html=etree.HTML(response)

#提取信息
title=html.xpath['']

#关闭浏览器
browser.quit()
#关闭chreomedriver进程
browser.close()