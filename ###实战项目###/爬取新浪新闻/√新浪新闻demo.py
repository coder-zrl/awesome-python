import requests
import wordcloud
import xlwt
import re
from urllib import parse
key_word = input('请输入关键字：')
kd = {'q': key_word}
strs = parse.urlencode(kd)
page_list = ['1', '2', '3', '4', '5','6','7']
url_lists=[]
for page in page_list:
    url = 'https://search.sina.com.cn/?' + strs + '&c=news&from=channel&col=&range=title&source=&country=&size=10&stime=&etime=&time=&dpc=0&a=&ps=0&pf=0&page=' + page
    response = requests.get(url, )
    text = response.text
    urls = re.findall(r'<a href="(https://k.sina.com.cn/article.*?)" target="_blank">', text)[:10]
    url_lists += urls

all_str=''
workbook=xlwt.Workbook()
worksheet=workbook.add_sheet('test')
for i in range(len(url_lists)):
    response = requests.get(url_lists[i]).content.decode()
    title = re.findall('<title>(.*?)</title>', response)[0]
    author = re.findall('<meta property="article:author" content="(.*?)"', response)[0]
    date = re.findall('<span class="date">(.*?)</span>', response)[0]
    main_text_demo = re.findall('<!-- 正文 start -->(.*?)<!-- 正文 end -->', response, re.DOTALL)[0]
    main_text = re.sub('<.*?>', '', main_text_demo)
    main_text = re.sub(r'\(.*\);', '', main_text)
    main_text = re.sub('\n', '', main_text)
    worksheet.write(i,0,title)
    worksheet.write(i,1,author)
    worksheet.write(i,2,date)
    worksheet.write(i,3,main_text)
    all_str+=main_text
    #print(title, author, date, main_text)
    print(title)
workbook.save('%s.xlsx'%key_word)


w = wordcloud.WordCloud(width=1200,height=600,font_path='msyh.ttc')
w.generate(all_str)
w.to_file("outfile.png")
