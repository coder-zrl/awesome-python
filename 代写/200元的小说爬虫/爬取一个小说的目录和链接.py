import requests
import re
# header={
# 'Connection': 'keep-alive',
# 'Host': 'www.shujy.com',
# 'Referer': 'https://www.shujy.com/fenlei/111/1.html',
# 'Upgrade-Insecure-Requests': '1',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
# }
url='https://www.shujy.com/5200/247205/'
response=requests.get(url).text
print(response)
title=re.findall('<h1>(.*?)</h1>',response)[0]
author=re.findall('<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>',response)[0]
detail_data=re.findall('<div id="intro">(.*?)</div>?',response,re.DOTALL)[0]
title_list=re.findall('<dd><a href=".*?">(.*?)</a>',response)
url_list_demo=re.findall('<dd><a href="(.*?)">.*?</a>',response)
url_list=[url+i for i in url_list_demo]
print(title)
print(author)
print(detail_data)
for i in zip(title_list,url_list):
    print(i)