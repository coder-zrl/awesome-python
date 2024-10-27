#110首
import requests
import re
count=0
with open('李清照诗词集.md','w',encoding='utf-8') as fp:
    for i in range(1,12):
        print('正在爬取第%d页'%i)
        url='https://so.gushiwen.org/authors/authorvsw.aspx?page='+str(i)+'&id=9cb3b7c0e4a0'
        response=requests.get(url).text
        # print(response)
        poem_title_list=re.findall('<textarea style=" background.*id=.*">?(.*》?)https',response)[:-1]
        count+=len(poem_title_list)
        for j in poem_title_list:
            data=j.split('——宋代·李清照')
            data.insert(1,'\n')
            data.reverse()
            data.insert(0,'# ')
            data.append('\n\n')
            fp.writelines(data)
print('共%d首诗词'%count)