import requests
import re
name_list=[]
url_list=[]
url='https://www.shujy.com/fenlei/111/'  # 一页30个
for i in range(1,35):
    print('正在爬取第%s页，共34页'%i)
    new_url=url+str(i)+'.html'
    response=requests.get(new_url).text
    name_list+=re.findall('《.*?>(.*?)</a>》',response)
    url_list_demo=re.findall('《<a href="(.*?)" target="_blank">.*?</a>》',response)
    url_list+=['https://www.shujy.com'+i for i in url_list_demo]
damo=zip(name_list,url_list)
for i in damo:
    print(i)
