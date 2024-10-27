import requests
import json
import datetime
nowTime=datetime.datetime.now().strftime('%Y-%m-%d')#现在
print(nowTime)

# url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage&qq-pf-to=pcqq.c2c'
# url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage'
# 还有一个http://ncov.deepeye.tech/
# https://news.qq.com/zt2020/page/feiyan.htm#/?pool=bj&nojump=2
url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341027523371041305267_1592721097964&_=1592721097965'

response=requests.get(url).text
first_index=response.find('(')
response=response[first_index+1:-1]
# re.findall('id="captain-config">',response)
data=json.loads(response)['data']
data=json.loads(data)['areaTree'][0]['children']  # 得到一个列表，里面是我们想要的信息
f=open('实时疫情-'+str(nowTime)+".csv",'w')
f.write("疫情地区,新增,现有,累计,治愈,死亡,\n")

for i in data:
    # print(i)
    name=i['name']  # 疫情地区
    if(i['today']['isUpdated']):
        today_add=i['today']['confirm']  # 新增
    else:
        today_add="今日未公布"
    nowConfirm=i['total']['nowConfirm']  # 现有
    confirm = i['total']['confirm']  # 累计
    heal = i['total']['heal']  # 治愈
    dead = i['total']['dead']  # 死亡
    one_data=[name,today_add,nowConfirm,confirm,heal,dead]
    one_data=[str(i) for i in one_data]
    print(one_data)
    data=','.join(one_data)+'\n'
    f.write(data)
    # print((name,today_add,nowConfirm,confirm,heal,dead))
    # print(i,data[i])
f.close()
