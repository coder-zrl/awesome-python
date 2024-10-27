# -*- coding: utf-8 -*-
# author: Jclian91
# time: 2020-01-29 11:37
# -*- coding: utf-8 -*-
# author: Jclian91
# time: 2020-01-29 11:37
# from pyecharts.globals import CurrentConfig
#
# CurrentConfig.ONLINE_HOST = "http://127.0.0.1:8000/assets/"
from pyecharts.charts import Map
from pyecharts import options as opts

# 省和直辖市
province_distribution = {'湖北':3554, '浙江':296, '广东': 241,
       '湖南':221, '河南':206, '安徽': 152,
       '重庆':147, '山东':121, '江西': 109,
       '四川':108, '江苏':99, '北京':91,
       '福建':82, '上海':80, '广西':58,
       '陕西':56, '河北':48, '云南':44,
       '海南':43, '黑龙江':37, '辽宁':36,
       '山西':27, '天津':25, '甘肃':24,
       '内蒙古':16, '新疆':13, '宁夏':12,
       '贵州':9, '吉林':9, '台湾':8,
       '香港':8, '澳门':7, '青海':6,
       '西藏':0
       }

# maptype='china' 只显示全国直辖市和省级
map = Map()
map.width='100'
map.height='150'
map.set_global_opts(
        title_opts=opts.TitleOpts(title="20200129中国疫情地图"),
        visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True,
          pieces=[
          {"max": 5000, "min": 1001, "label": ">1000", "color": "#8A0808"},
          {"max": 1000, "min": 500, "label": "500-1000", "color": "#B40404"},
          {"max": 499, "min": 100, "label": "100-499", "color": "#DF0101"},
          {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
          {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
          {"max": 0, "min": 0, "label": "0", "color": "#FFFFFF"},
          ], ) #最大数据范围，分段
 )
map.add("20200129中国疫情地图", data_pair=list(province_distribution.items()), maptype="china", is_roam=True)
map.render('20200129中国疫情地图.html')