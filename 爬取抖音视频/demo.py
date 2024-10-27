import requests

url='https://v.douyin.com/J2EarSN/'
resp=requests.get(url).text
print(resp)
