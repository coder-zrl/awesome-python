from pyecharts.charts import Map
from pyecharts import options as opts
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from matplotlib import font_manager
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")  # 设置字体为微软雅黑
import requests
import re
import json
import math  # 正无穷
url='https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=jQuery341027523371041305267_1592721097964&_=1592721097965'
response=requests.get(url).text
first_index=response.find('(')
response=response[first_index+1:-1]
data=json.loads(response)['data']
data=json.loads(data)['areaTree'][0]['children']  # 得到一个列表，里面是我们想要的信息
province=[]  # 疫情地区
today_add=[]  # 新增
nowConfirm=[]  # 现有
for i in data:
    province.append(i['name'])  # 疫情地区
    today_add.append(i['today']['confirm'])  # 新增
    nowConfirm.append(i['total']['nowConfirm'])  # 现有


url='https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=singlemessage'
response=requests.get(url).text
data_demo=re.findall('<script(.*?)</script>',response)[6]
data=re.findall('({"confirmed":".*?","died":".*?","crued":".*?","relativeTime".*?),"subList"',data_demo)[:34]
data=[i+'}' for i in data]
contrast={}  # 对照的数据
for i in data:
    i=json.loads(i)
    ne=i['area']  # 疫情地区
    to_ad=i['confirmedRelative']  # 新增
    contrast[ne]=to_ad


contrast_province=[]
for i in range(len(province)):
    for j in contrast.items():
        if province[i]==j[0]:
            contrast_province.append(province[i]+str(j[1]))
# 直方图
plt.figure(figsize=(16, 7))  # 设置图片初始化大小
p1 = plt.bar(x=contrast_province, height=today_add)
plt.xticks(contrast_province,fontproperties=my_font)
plt.title('各省份每日增长数据', fontproperties=my_font)
plt.xlabel('省份', fontproperties=my_font)
plt.ylabel('日增(人)', fontproperties=my_font)
plt.savefig('各省份每日增长数据.png',dip=400)
plt.show()

# 地图
map = Map()
map.set_global_opts(
        title_opts=opts.TitleOpts(title="中国疫情地图"),
        visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
        pieces=[
          {"max": math.inf, "min": 10000, "label": ">=1000", "color": "#8A0808"},
          {"max": 9999, "min": 1000, "label": "1000-9999", "color": "#B40404"},
          {"max": 999, "min": 100, "label": "100-999", "color": "#DF0101"},
          {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
          {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
          {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
          ], ) #最大数据范围，分段
 )
map.add("中国疫情地图", data_pair=list(zip(province,nowConfirm)), maptype="china", is_roam=True)
map.render('中国疫情地图.html')