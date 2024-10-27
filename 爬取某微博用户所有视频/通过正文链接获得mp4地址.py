import requests
import re
# 正文链接https://m.weibo.cn/status/4512733603289126?#&video

headers={
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'
}
url = "https://m.weibo.cn/status/4512733603289126?"
response=requests.get(url,headers=headers).text
print(response)
download_url=re.findall('"stream_url_hd": "(.*?)",',response)[0]
download_title=re.findall('"status_title": "(.*?)",',response)[0]
video_response=requests.get(download_url).content
with open(download_title+'.mp4','wb') as fp:
    fp.write(video_response)
print(download_url)
print(download_title)