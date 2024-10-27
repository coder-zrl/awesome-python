import requests
import re  # 正则表达式
import json
import datetime
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
nowTime=datetime.datetime.now().strftime('%Y-%m-%d')#现在
print(nowTime)

url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage'
response=requests.get(url).text
data_demo=re.findall('<script(.*?)</script>',response)[6]  # 提取信息
data=re.findall('({"confirmed":".*?","died":".*?","crued":".*?","relativeTime".*?),"subList"',data_demo)[:34]
data=[i+'}' for i in data]

f=open('实时疫情-'+str(nowTime)+".csv",'w')
f.write("疫情地区,新增,现有,累计,治愈,死亡,\n")
add_pvice={}
for i in data:
    i=json.loads(i)
    # print(i)
    # confirmed 830
    # died 9
    # crued 584
    # relativeTime 1592668800
    # confirmedRelative 9
    # diedRelative 0
    # curedRelative 0
    # confirmInter 1
    # curConfirm 237
    # curConfirmRelative 9
    # cityCode 131
    # icuDisable 1
    # area 北京
    # for j in i:
    #     print(j,i[j])
    name=i['area']  # 疫情地区
    today_add=i['confirmedRelative']  # 新增
    if today_add!='0':
        add_pvice[name]=int(today_add)
    nowConfirm=i['curConfirm']  # 现有
    confirm = i['confirmed']  # 累计
    heal = i['crued']  # 治愈
    dead = i['died']  # 死亡
    one_data = [name, today_add, nowConfirm, confirm, heal, dead]
    one_data = [str(i) for i in one_data]
    print(one_data)
    data = ','.join(one_data) + '\n'
    f.write(data)
    # print((name,today_add,nowConfirm,confirm,heal,dead))
f.close()
ls=list(add_pvice.items())
ls.sort(key=lambda x:x[1],reverse=True)
add_pvice=dict(ls)
p1 = plt.bar(add_pvice.keys(), add_pvice.values())
plt.savefig('实时疫情-'+str(nowTime)+".png")
plt.show()




