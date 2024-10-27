import requests
url='https://www.jisilu.cn/data/cbnew/cb_list/?___jsl=LST___t=1592725044171'
response=requests.get(url).text
print(response)