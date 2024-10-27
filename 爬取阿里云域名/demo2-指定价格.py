import requests
import json


#页数currentPage

#长度minLength,maxLength
length=[i for i in range(1,11)]
#组成constitute  11-16


params={
'fetchSearchTotal': 'true',
'token': 'tdomain-aliyun-com:dcwvpkq1SI4dut3lmTGEecpSH0yntold',
'pageSize': '200',

'currentPage':'1',
'productType': '2',
'minLength':'null',
'maxLength':'null',
'minPrice':'null',
'maxPrice':'null',
'constitute':'null',

'searchIntro':'false',
'keywordAsPrefix': 'false',
'keywordAsSuffix': 'false',
'exKeywordAsPrefix': 'false',
'exKeywordAsSuffix': 'false',
'exKeywordAsPrefix2': 'false',
'exKeywordAsSuffix2': 'false',
'callback': 'jQuery1113046389565255238296_1598778601338'
}

headers={
'authority': 'domainapi.aliyun.com',
'method': 'GET',
'path': '/onsale/search?fetchSearchTotal=true&token=tdomain-aliyun-com:dcwvpkq1SI4dut3lmTGEecpSH0yntold&currentPage=1&pageSize=50&productType=2&searchIntro=false&keywordAsPrefix=false&keywordAsSuffix=false&exKeywordAsPrefix=false&exKeywordAsSuffix=false&exKeywordAsPrefix2=false&exKeywordAsSuffix2=false&callback=jQuery1113046389565255238296_1598778601338&_=1598778601339',
'scheme': 'https',
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'zh-CN,zh;q=0.9',
'cookie': 'cna=1D2lFz7l4xUCAW7lFQKHl6pe; aliyun_choice=CN; UM_distinctid=173a88d97261c9-06e28b908ed3f8-59492816-1fa400-173a88d97282de; xlly_s=1; JSESSIONID=R3666HD1-CB7IWYWYYSH5B0WX71TC2-G3BUUGEK-OMX47; _ga=GA1.2.536758830.1598778481; _gid=GA1.2.906470678.1598778481; _s0=eNrz4A12DQ729PeL9%2FV3cfUxiKvOTLFSCjI2MzPzcDHUdXYy9wyPDI%2BMDPYwdTIIjzA3DHE20nU3dgoNdXf11vX3jTAxV9JJLrEyNLW0MDc3N7EE0gY6iclQAQtTQ3MjEyOd3AorQwsDg9ooAKpEHUg%3D; l=eBOXimJROEonWGAMmOfwourza77OSIRAguPzaNbMiOCPt9XB5uuNWZPiqoK6C3GVhsGpR3ljL4J_BeYBqSmfZDr7Hv6wsCDmn; tfstk=cnoPBnAbL3Kz2nEBWuZFAeY4RkN5ZIkoKiy_r2m6mpNdRWUliVfLhZab3J95Fzf..; isg=BOzsKP0yn_Qu1IudNkmEaaUGvcoepZBP7laBpUYt-Bc7UYxbbrVg3-JncRlpWcin',
'referer': 'https://mi.aliyun.com/?spm=5176.8006371.772227.ymzcjy.5d907e63MzMfcr',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36'
}

url='https://domainapi.aliyun.com/onsale/search'


#价格
for i in range(90001,100000,5000):
    print(i)
    real_params=params.copy()
    # 设置价格范围
    real_params['minPrice'] = str(i)
    real_params['maxPrice'] = str(i+5000)
    #组成
    for j in [11,12,13,14,15,16]:
        real_params['constitute']=str(j)
        #长度
        for k in range(1,11):
            if k==10:
                real_params['minLength']=str(k)
                real_params['maxLength'] = 'null'
            else:
                real_params['minLength']=str(k)
                real_params['maxLength'] = str(k)
            # 页数
            for l in range(1,26):
                real_params['currentPage']=str(l)

                response=requests.get(url,headers=headers,params=real_params).text[:-2]
                response=response.strip(params['callback']+"(")
                try:
                    data=json.loads(response)['data']['pageResult']['data']
                    with open('data.csv','a') as fp:
                        for one_data in data:
                            yuming=one_data['domainName']
                            price=one_data['price']
                            fp.writelines([yuming,',',price.replace(',',''),',','\n'])
                            print(yuming,price)
                except:
                    break