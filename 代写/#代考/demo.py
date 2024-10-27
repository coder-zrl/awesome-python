import requests
import re
from bs4 import BeautifulSoup
headers2={
'Host': 'weibo.com',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
'Accept': '*/*',
'Accept-Language': 'en-GB,en;q=0.5',
'Accept-Encoding': 'gzip, deflate, br',
'Content-Type': 'application/x-www-form-urlencoded',
'X-Requested-With': 'XMLHttpRequest',
'Connection': 'keep-alive',
'Referer': 'https://weibo.com/hejiong?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1',
'Cookie': 'SINAGLOBAL=9966933033334.297.1574994494415; ULV=1594565656576:39:3:3:1523923498028.8486.1594565656571:1594488212164; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWMKey-sORcS850A3xjWe005JpX5KzhUgL.FoqX1hBReKe7e0-2dJLoIp7LxKML1KBLBKnLxKqL1hnLBoMcShnX1h20ehef; SUHB=0QS5awTKX9wFjN; UOR=,,www.baidu.com; SCF=ApBBedCvAoSMBdRROlieaWW13D8VchMSFK2LF6moAfSnyHGv7hHiWqi4JZ0QaBArNRAJzRR64s8VHlUxdYicZ5s.; ALF=1626101650; wb_view_log=1451*9071.7647058823529411; un=15007451623; wb_view_log_6484813035=1451*9071.7647058823529411; webim_unReadCount=%7B%22time%22%3A1594568389560%2C%22dm_pub_total%22%3A0%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A6%2C%22msgbox%22%3A0%7D; Ugrow-G0=5c7144e56a57a456abed1d1511ad79e8; SUB=_2A25yD1RDDeRhGeBK41YZ8S3MyDmIHXVRfcKLrDV8PUNbmtANLXPakW9NR2sge4AxYh3uNmuzGk3lV3qrRlcTdbY5; SSOLoginState=1594565650; wvr=6; YF-V5-G0=b588ba2d01e18f0a91ee89335e0afaeb; _s_tentry=login.sina.com.cn; Apache=1523923498028.8486.1594565656571; YF-Page-G0=4358a4493c1ebf8ed493ef9c46f04cae|1594568268|1594568243; wb_timefeed_6484813035=1'
        }
src = "https://weibo.com/hejiong?is_search=0&visible=0&is_all=1&is_tag=0&profile_ftype=1&page=1#feedtop"
#src2 = "https://cloud.tencent.com/developer/ask/176101"
res = requests.get(src,headers = headers2)
rest=res.text
print(rest)
data_demo=re.findall('<div id=\"Pl_Official_MyProfileFeed__21\" anchor=\"-50\">(.*?)<div id=\"Pl_Official_TimeBase__22\" anchor=\"-50\">',rest,re.DOTALL)[0]
print(data_demo)
# print(res.text)

# html = str(res.text)
# soup=BeautifulSoup(html,'html.parser')
# contexts=soup.select(".media_box")
# print(contexts)