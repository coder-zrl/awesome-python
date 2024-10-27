import time
from selenium import webdriver

driver = webdriver.Chrome()

# 强制等待
def wait1():
    #强制等待
    time.sleep(5)

#隐式等待
def wait2():
    #设置隐式等待，隐性等待对整个driver的周期都起作用，所以只要设置一次即可。放在get上面
    #有一个弊端：程序会一直等待整个页面加载完成，即你看到浏览器标签栏那个小圈不再转，才会执行下一步
    driver.implicitly_wait(10)
    driver.get('www.baidu.som')

# 显式等待,只要出现想要的那个元素就停止等待
def wait3():
    #显示等待。第3秒就找到了这个元素，那么也就不会多等剩下的7秒使时间，而是继续执行后续代码。
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    try:
        element = WebDriverWait(driver, 10,0.5).until(
            EC.presence_of_element_located((By.ID, "myDynamicElement"))
        )
        #10代表如果10秒还不出来就算超时，0.5代表检查间隔时间（步长），默认为0.5
    finally:
        driver.quit()
    '''
    一些其他的等待条件：
    presence_of_element_located：某个元素已经加载完毕了。
    presence_of_all_emement_located：网页中所有满足条件的元素都加载完毕了。
    element_to_be_cliable：某个元素是可以点击了
    '''
