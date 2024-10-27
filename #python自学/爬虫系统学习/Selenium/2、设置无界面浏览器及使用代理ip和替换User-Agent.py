from selenium import webdriver


chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument('--praxy-srever=http://171.12.313.34:9999')#设置代理ip
chrome_options.add_argument('--user-agent=')#设置user-agent，可以设置成手机端的
chrome_options.add_argument('--headless')#设置无页面模式
browser = webdriver.Chrome(options=chrome_options)

# 开始请求
url = "https://www.baidu.com"
browser.get(url)
#打印页面源代码
print(browser.page_source)
#关闭浏览器
browser.quit()
#关闭chreomedriver进程