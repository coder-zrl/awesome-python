from selenium import webdriver
driver = webdriver.Chrome()

#模拟向下滑动，记得做循环
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")#先下滑到底    0代表坐标
driver.execute_script("window.scrollTo(1000,document.body.scrollHeight)")#再上滑一下    1000代表坐标

'''
window.scrollBy(0,500)　　   向下滚动500个像素
window.scrollBy(0,-500)　　 向上滚动500个像素
window.scrollBy(500,0)　　   向右滚动500个像素
window.scrollBy(-500,0)　　 向左滚动500个像素
'''


#行为链模拟按键
# ActionChains(driver).key_down(Keys.DOWN).perform()

#输入查询的字，可以根据id、class_name、name、tag_name、xpath、css选择器来选择，具体看你想弄的地方有什么可选的
inputTag = driver.find_element_by_class_name('tt-input__inner')
inputTag.send_keys('银行')

#点击搜索
inputTag = driver.find_element_by_xpath('tt-input-group__append')
inputTag.click()

#切换浏览器页面。因为虽然显示带开了新页面，但url信息并不会转移到新页面
windows=driver.window_handles#得到当前所有窗口
driver.switch_to.window(windows[1])#根据索引进行选择

#访问frame标签。即html中嵌套了新的html，例如QQ空间
login_frame=driver.find_element_by_id('login_frame')#定位到framde的位置
driver.switch_to.frame(login_frame)#切换至frame中，然后就能对frame里面的东西进行操作了

#页面截图
driver.save_screenshot('到此一游.png')

#获取cookie
print(driver.get_cookies())#得到列表，不仅包含name，value还包含其他信息
cookie_dict={cookie['name']:cookie['value'] for cookie in driver.get_cookies()}#通常这样配合requests库使用cokie信息