import requests
import re  # 正则表达式
import json
# url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage&qq-pf-to=pcqq.c2c'
url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage'

response=requests.get(url).text
# print(response)
data_demo=re.findall('<script(.*?)</script>',response)[6]  # 提取信息
data=re.findall('({"confirmed":".*?","died":".*?","crued":".*?","relativeTime".*?),"subList"',data_demo)[:34]

# for i in data_demo:
#     print(data_demo.index(i),i)
#     print('*'*60)
# area
#
data=[i+'}' for i in data]
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
    nowConfirm=i['curConfirm']  # 现有
    confirm = i['confirmed']  # 累计
    heal = i['crued']  # 治愈
    dead = i['died']  # 死亡
    print((name,today_add,nowConfirm,confirm,heal,dead))




