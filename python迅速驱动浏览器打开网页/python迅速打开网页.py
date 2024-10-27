import sys
import webbrowser
sys.path.append("libs")
url = 'https://www.toutiao.com/'
webbrowser.open(url)

'''
import webbrowser
webbrowser.open(‘http://www.baidu.com’,new=0,autoraise=True)
#new:0/1/2 0：同一浏览器窗口打开 1：打开浏览器新的窗口，2：打开浏览器窗口新的tab 
#autoraise=True:窗口自动增长

webbrowser.open_new(‘http://www.baidu.com’)
webbrowser.open_new_tab(‘http://www.baidu.com’)

web.get(name)：获取打开的浏览器对象，name为空，则打开默认的浏览器，name为浏览器名称
直接打开则会报错，需要注册浏览器对象
web.register()：注册浏览器类型
import webbrowser as web
chromepath = 'C:\***\***\***\***\Google\Chrome\Application\chrome.exe'            
#例如我的：C:\***\***\***\***\Google\Chrome\Application\chrome.exe  
web.register('chrome', None, webbrowser.BackgroundBrowser(chromepath))  
web.get('chrome').open_new_tab('www.baidu.com') 
'''
