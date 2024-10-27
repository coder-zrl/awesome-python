import requests
import json

url = 'http://webapi.http.zhimacangku.com/getip?num=1&type=2&pro=130000&city=130500&yys=0&port=1&pack=100227&ts=0&ys=0&cs=0&lb=1&sb=0&pb=4&mr=1&regions='
response = requests.get(url).text
data = json.loads(response)
ip = data['data'][0]['ip']
port = data['data'][0]['port']
print(ip, port)

proxy = {
    'http':'120.14.29.49:4267'
}
headers={}
response=requests.get('http://httpbin.org/ip',headers=headers,proxies=proxy)
print(response.text)
