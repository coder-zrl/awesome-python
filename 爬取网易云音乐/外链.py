'''
http://music.163.com/song/media/outer/url?id=1383927243
'''
import re
import requests
id=input('请输入网址:')
id=re.findall('(id=\d*)',id)[0]
# print(id)
url='http://music.163.com/song/media/outer/url?'+id
print(url)
response=requests.get(url).text
print(response)
# with open('music.mp3','wb') as fp:
#     fp.write(response)