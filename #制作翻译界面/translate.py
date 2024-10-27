def transtale_result(strs):
    import requests
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
    data={
        'i': strs,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    response=requests.post(url,data,headers=headers)
    result=response.json()['translateResult'][0][0]
    return str(result.get('tgt'))