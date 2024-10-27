import requests
import time
from selenium import webdriver
import re
acct_num=input('输入用户号')
begin=int(input('输入起始页：'))
end=int(input('输入终止页'))
req_url_list=[]
url_name=[]
for i in range(begin,end+1):
    req_url_list.append('https://weibo.com/'+acct_num+'/?page='+str(i))
driver = webdriver.Chrome()
for req_url in req_url_list:
    # 开始请求
    driver.get(req_url)
    time.sleep(5)
    for i in range(10):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # 先下滑到底    0代表坐标
        driver.execute_script("window.scrollTo(1000,document.body.scrollHeight)")  # 再上滑一下    1000代表坐标
        time.sleep(0.3)
    data=driver.page_source
    url_name+=re.findall('name=(\d{16}?) target',data)+re.findall('name="(\d{16}?)" target',data)


url_list=['https://m.weibo.cn/status/'+i for i in url_name]
for i in url_list:
    print(i)
headers={
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
for url in url_list:
    try:
        response=requests.get(url,headers=headers).text
        # print(response)
        download_url=re.findall('"stream_url": "(.*?)",',response)[0]  # stream_url_hd
        download_title=re.findall('"status_title": "(.*?)",',response)[0]
        download_title=re.sub('#.*?#',download_title)[0]
        if download_title ==' ':
            download_title='哈'*20
        video_response=requests.get(download_url).content
        with open('./视频/'+download_title+'.mp4','wb') as fp:  #
            fp.write(video_response)
        print(download_url)
        print(download_title)
    except:
        pass