import requests
import re
url_list=[]
url='https://www.shujy.com/fenlei/111/'  # 一页30个
for i in range(1,35):
    print('正在爬取第%s页，共34页'%i)
    new_url=url+str(i)+'.html'
    response=requests.get(new_url).text
    url_list_demo=re.findall('《<a href="(.*?)" target="_blank">.*?</a>》',response)
    url_list+=['https://www.shujy.com'+i for i in url_list_demo]
for i in url_list:
    response = requests.get(i).text
    title = re.findall('<h1>(.*?)</h1>', response)[0]
    author = re.findall('<p>作&nbsp;&nbsp;&nbsp;&nbsp;者：(.*?)</p>', response)[0]
    detail_data = re.findall('<div id="intro">(.*?)</div>?', response, re.DOTALL)[0]
    title_list = re.findall('<dd><a href=".*?">(.*?)</a>', response)
    url_list_demo = re.findall('<dd><a href="(.*?)">.*?</a>', response)
    url_list = [i + t for t in url_list_demo]
    f = open('小说章节爬取.txt', 'a')
    print(title)
    print(author)
    print(detail_data)
    f.writelines([title+'\n',author+'\n',detail_data+'\n'])
    for i in zip(title_list, url_list):
        print(i[0],i[1])
        f.writelines([i[0],i[1]+ '\n'])