import requests
import json
url='http://cn.morningstar.com/handler/quicktake.ashx?command=rating&fcid=0P0000WEF3'
response=requests.get(url).text
data=json.loads(response)#得到了列表形式的数据，再去提取  data.keys()得到的是键的列表