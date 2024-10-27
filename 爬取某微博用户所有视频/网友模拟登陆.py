import requests
import re
import json
# 正文链接https://m.weibo.cn/status/4512733603289126?#&video

headers = {
    'Cookie': '_T_WM=12245567899; SCF=AtLxWPsA90jcDb8gEJ2POtGvKEx0DBDJ1hcWgddgqiPr3PLm5O5WqZY-QSH46rHbLb205LidSdy6OKboOk2BaWU.; SUHB=0cS3x1-XKtKMo9; ALF=1594217493; XSRF-TOKEN=ffed91; WEIBOCN_FROM=1110006030; MLOGIN=0; M_WEIBOCN_PARAMS=luicode%3D10000011%26lfid%3D100103type%253D1%2526q%253D%25E6%2596%25B0%25E5%2586%25A0%25E7%2597%2585%25E6%25AF%2592%26fid%3D100103type%253D1%2526q%253D%25E6%2596%25B0%25E5%2586%25A0%25E7%2597%2585%25E6%25AF%2592%26uicode%3D10000011',
    'Referer': 'https://m.weibo.cn/search?containerid=100103type%3D1%26q%3D%E6%96%B0%E5%86%A0%E7%97%85%E6%AF%92&display=0&retcode=6102',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

data={
'containerid': '100103type=1&q=新冠病毒',
'page_type': 'searchall',
'page': '2'
}
url = "https://m.weibo.cn/api/container/getIndex?containerid=100103type%3D1%26q%3D%E6%96%B0%E5%86%A0%E7%97%85%E6%AF%92&display=0&retcode=6102&page_type=searchall"
response=requests.get(url,headers=headers,params=data).content.decode()
data=json.loads(response)['data']['cards']
for i in data:
    print(i)
print(response)
# download_url=re.findall('"stream_url_hd": "(.*?)",',response)[0]
# download_title=re.findall('"status_title": "(.*?)",',response)[0]
# video_response=requests.get(download_url).content
# with open(download_title+'.mp4','wb') as fp:
#     fp.write(video_response)
# print(download_url)
# print(download_title)