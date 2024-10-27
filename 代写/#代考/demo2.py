#wx1.sinaimg.cn%2Forj360%2F473dc466gy1gg869j7wqaj234g34gkjt.jpg
import requests
import re
url='https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100306&is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__21&id=1003061195230310&script_uri=/hejiong&feed_type=0&pre_page=1&domain_op=100306&__rnd=1594573468834'
response=requests.get(url).content.decode()
print(response)
urls=re.findall(r'wx1\.sinaimg\.cn%2.*%2F473dc466gy1gg869j7wqaj234g34gkjt\.jpg',response)
[print(i) for i in urls]
