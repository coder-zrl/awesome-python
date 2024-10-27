from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
# pip uninstall selenium后安装低版本的 pip install selenium==2.48.0
#因为高版本的已经放弃phantomjs了
# phantomjs浏览器
# dcap = dict(DesiredCapabilities.PHANTOMJS)
# dcap['phantomjs.page.settings.userAgent'] = \
#     ('Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36')
# driver = webdriver.PhantomJS(executable_path=r"C:\Users\86166\AppData\Local\Programs\Python\Python37-32\phantomjs-2.1.1-windows\bin\phantomjs.exe", desired_capabilities=dcap,
#                              service_args=['--ignore-ssl-errors=true'])

#或者直接就好
driver = webdriver.PhantomJS(executable_path=r"C:\Users\86166\AppData\Local\Programs\Python\Python37-32\phantomjs-2.1.1-windows\bin\phantomjs.exe")

driver.get(url)
