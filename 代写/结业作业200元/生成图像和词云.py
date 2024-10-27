import requests
import jieba
# import wordcloud
import numpy as np
import re
import matplotlib; matplotlib.use('TkAgg')
from matplotlib import font_manager
# 中文字体准备
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")  # 设置字体为微软雅黑
import matplotlib.pyplot as plt

# # 直方图
# N=5
# y=[20,10,30,25,15]
# index = np.arange(N)
# # bottom 指的是最底层坐标
# p1 = plt.bar(x=index, height=y,width=0.5,bottom=100,color=15138834)
# plt.show()
# # 绘制水平条形图写上这个参数orientation='horizontal'
# p2 = plt.bar(x=0, bottom=index, width=y,height=0.5,orientation='horizontal')
# # 或者写成p2 = plt.barh(x=0, bottom=index, width=y,height=0.5,orientation='horizontal')
# plt.show()


def get_danmu(cid=63369190):  # 调用api获取指定cid视频的弹幕  63369190
    # 或者http://comment.bilibili.com/{cid}.xml
    url = 'http://api.bilibili.com/x/v1/dm/list.so?oid='+str(cid)
    print(url)
    response = requests.get(url).content.decode()  # 出现乱码问题，需要解码再重新编码
    related_attributes = re.findall('p="(.*?)"', response)  # 提取d标签p属性的内容
    barrages = re.findall('">(.*?)</d>?', response)  # 提取弹幕
    # 弹幕在视频出现的时间，单位是秒
    barrage_sending_time=[]
    # 弹幕类型，123普通，4底部，5顶部，6逆向，7精准定位，8代码位置，9BAS弹幕
    barrage_type=[]
    # 弹幕字号，18小，25标准，36大
    barrage_size=[]
    # 弹幕颜色，十进制RGB888值
    barrage_color=[]
    # 弹幕发送时间，时间戳
    sending_time=[]
    # 弹幕池类型 0普通池，1字幕池，2特殊池子（高级弹幕）
    barrage_pool_type=[]
    # 返回HEX类型数据，用于屏蔽用户和查看用户发送的所有弹幕，也可反差用户ID
    encoded_users=[]
    # 弹幕ID
    barrage_id=[]
    for related_attribute in related_attributes:
        one_barrage_of_data=related_attribute.split(',')
        barrage_sending_time.append(one_barrage_of_data[0])
        barrage_type.append(one_barrage_of_data[1])
        barrage_size.append(one_barrage_of_data[2])
        barrage_color.append(one_barrage_of_data[3])
        sending_time.append(one_barrage_of_data[4])
        barrage_pool_type.append(one_barrage_of_data[5])
        encoded_users.append(one_barrage_of_data[6])
        barrage_id.append(one_barrage_of_data[6])
    print(barrage_type)
    print(barrages)
    return barrage_color



def type():
    def count(mylist):
        mydict = {'普通': 0, '底部': 0, '顶部': 0, '逆向': 0, '精准定位': 0, '代码位置': 0, 'BAS弹幕': 0}
        for i in mylist:
            if '0' <= i <= '3':
                mydict['普通'] += 1
            elif i == '4':
                mydict['底部'] += 1
            elif i == '5':
                mydict['顶部'] += 1
            elif i == '6':
                mydict['逆向'] += 1
            elif i == '7':
                mydict['精准定位'] += 1
            elif i == '8':
                mydict['代码位置'] += 1
            elif i == '9':
                mydict['BAS弹幕'] += 1
        return list(mydict.keys()), list(mydict.values())
    barrage_type=get_danmu()
    barrage_type,type_count=count(barrage_type)
    print(barrage_type)
    print(type_count)
    plt.bar(x=barrage_type, height=type_count)
    plt.xticks(barrage_type, fontproperties=my_font)
    plt.title('弹幕类型图',fontproperties=my_font)
    plt.show()
def top10():
    def count(mylist):
        mydict={}
        for i in mylist:
            mydict[i]=mydict.get(i,0)+1
        mylist=list(mydict.items())
        mylist.sort(key=lambda x:x[1],reverse=True)
        barrage=[i[0] for i in mylist[:10]]
        frequency = [i[1]for i in mylist[:10]]
        return barrage,frequency

    # plt.rcParams['figure.figsize'] = (16.0, 7.0)
    plt.figure(figsize=(16, 7))
    barrages=get_danmu()
    barrage,frequency=count(barrages)
    plt.bar(x=barrage, height=frequency)
    plt.xticks(barrage, fontproperties=my_font)
    plt.title('弹幕Top10',fontproperties=my_font)
    plt.show()

def color():
    def count(mylist):
        color_dict1={'16646914':'#FE0302',
                    '16740868':'#FF7204',
                    '16755202':'#FFAA02',
                    '16765698':'#FFD302',
                    '16776960':'#FFFF00',
                    '10546688':'#A0EE00',
                    '52480':'#00CD00',
                    '104601':'#019899',
                    '4351678':'#4266BE',
                    '9022215':'#89D5FF',
                    '13369971':'#CC0273',
                    '2236962':'#222222',
                    '10197915':'#9B9B9B',
                    '16777215':'#FFFFFF'}

        color_dict={'16646914':'红色',
                    '16740868':'橘红',
                    '16755202':'橘黄',
                    '16765698':'淡黄',
                    '16776960':'黄色',
                    '10546688':'草绿',
                    '52480':'绿色',
                    '104601':'墨绿',
                    '4351678':'紫色',
                    '9022215':'青色',
                    '13369971':'品红',
                    '2236962':'黑色',
                    '10197915':'灰色',
                    '16777215':'白色'}
        mydict = {}
        for i in mylist:
            mydict[i] = mydict.get(i, 0) + 1
        print(mydict)
        for i in mydict.copy():
            try:
                mydict[color_dict[i]]= mydict[i]
                del mydict[i]
            except:
                mydict['其他色'] = mydict.get(i,0)+1
                del mydict[i]

        mylist = list(mydict.items())
        mylist.sort(key=lambda x: x[1], reverse=True)
        colors = [i[0] for i in mylist[:10]]
        frequency = [i[1] for i in mylist[:10]]
        return colors, frequency

    # plt.rcParams['figure.figsize'] = (16.0, 7.0)
    # plt.figure(figsize=(16, 7))
    barrages = get_danmu()
    colors, frequency = count(barrages)
    plt.bar(x=colors[0:1], height=frequency[0:1],width=0.3,color='#019899')
    plt.bar(x=colors[1:2], height=frequency[1:2], width=0.3)
    plt.xticks(colors, fontproperties=my_font)
    plt.title('弹幕颜色类型图', fontproperties=my_font)
    plt.show()


def could():
    def count(barrages_list):
        lastlist=[]
        for barrage in barrages_list:
            lastlist+=jieba.lcut(barrage)
        # mydict = {}
        # for i in lastlist:
        #     mydict[i] = mydict.get(i, 0) + 1
        # mylist = list(mydict.items())
        # mylist.sort(key=lambda x: x[1], reverse=True)
        laststr=' '.join(lastlist)
        return laststr

    # plt.rcParams['figure.figsize'] = (16.0, 7.0)
    # plt.figure(figsize=(16, 7))
    barrages = get_danmu()
    laststr = count(barrages)
    w = wordcloud.WordCloud(width=2000,height=1000,font_path='msyh.ttc')
    # w.generate(txt)向WordCloud对象w中加载文本txt
    w.generate(laststr)
    # w.to_file(filename) #将词云输出为图像文件,png或jpg格式
    w.to_file("outfile.png")


def progress():
    def count(barrage_sending_time):
        mydict = {}
        for i in range(0,int(barrage_sending_time[-1])+1):
            for t in barrage_sending_time:
                if i<=t<=i+1:
                    mydict[i] = mydict.get(i, 0) + 1
        time=list(mydict.keys())
        frequency=(mydict.values())
        return time,frequency

    # plt.figure(figsize=(16, 7))
    barrage_sending_time = get_danmu()
    print(barrage_sending_time)
    barrage_sending_time=[eval(i) for i in barrage_sending_time]
    barrage_sending_time.sort()
    time,frequency=count(barrage_sending_time)
    plt.bar(x=time, height=frequency)
    plt.xticks(time, fontproperties=my_font)
    plt.title('高能进度条',fontproperties=my_font)
    plt.show()

color()

