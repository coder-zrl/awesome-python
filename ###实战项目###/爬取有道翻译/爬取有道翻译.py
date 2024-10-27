#F12  在All中发现，点了翻译，一共有四步
#点开第一个发现为POST方式
#response是服务器响应得到的
#连接url，模拟请求，就能获得相应，，需要useaent来模拟人工操作
import requests
# url='http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
#去掉'_o'可以访问老版本，就不会被加密了
url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
contant=input('请输入你想翻译的内容：')
data={
    'i': contant,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    #salt: 15858988544861
    #sign: f49fc88600ff3f260a72b429cb4dada9
    #ts: 1585898854486
    #bv: b016bfc8dd420bcfc5d5a95c5a1600f4
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTION'
}
response=requests.post(url,data,headers=headers)
#整理数据
# print(response.text)
# print(response.json()['translateResult'][0][0])
result=response.json()['translateResult'][0][0]
print('翻译的结果是：%s'%result.get('tgt'))