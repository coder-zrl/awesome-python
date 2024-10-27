import requests
#登录的网站
url=''
#账号和密码
data={}
headers={}
session=requests.session()
session.post(url,data=data,headres=headers)
'''
已完成，已经登陆并获得cookie，并且已经储存，下次访问就不需要再在头文件里写cookie
'''
#找到必须登录才能进入的网站
new_url=''
response=requests.get(new_url,headers=headers)

