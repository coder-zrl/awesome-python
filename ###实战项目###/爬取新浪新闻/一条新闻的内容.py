import requests
import re
url='https://k.sina.com.cn/article_1343692175_50171d8f01900r1dz.html?from=health'
print(url)
response=requests.get(url).content.decode()
print(response)
title=re.findall('<title>(.*?)</title>',response)[0]
author=re.findall('<meta property="article:author" content="(.*?)"',response)[0]
date=re.findall('<span class="date">(.*?)</span>',response)[0]
main_text_demo=re.findall('<!-- 正文 start -->(.*?)<!-- 正文 end -->',response,re.DOTALL)[0]
main_text=re.sub('<.*?>','',main_text_demo)
main_text=re.sub(r'\(.*\);','',main_text)
main_text=re.sub('\n','',main_text)
print(title,author,date,main_text)

# print(response)