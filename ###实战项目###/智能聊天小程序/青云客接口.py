# http://api.qingyunke.com/
import requests
while True:
    message=input('你说：')
    if message=='拜拜':
        break
    url=f'http://api.qingyunke.com/api.php?key=free&appid=0&msg={message}'
    # print(url)
    # print(requests.get(url).text)#  输入你好呀。得到{"result":0,"content":"你好我才好"}
    response=requests.get(url).json()['content']
    # print(response)
    result=response.replace('{br}','\n')
    print(result)