import requests
from lxml import etree

headers={

}

params={

}

url = "https://www.baidu.com"
#得到页面源代码
response=requests.get(url,headers=headers,params=params)
html=etree.HTML(response.text)   #response.contect().decode('utf-8')
#提取信息
title=html.xpath('')
