import requests

# headers={
# 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'
# }
data={
'phone': '16603242019',
'countryCode': '+86',
'isoCode': 'cn'
}
#哈喽


url_list=['https://codemart.com/api/account/verification-code']
response=requests.post(url_list[0],data=data)  #,headers=headers
print(response.text)
