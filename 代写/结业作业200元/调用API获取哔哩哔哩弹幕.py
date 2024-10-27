import requests
import re
import json
# https://github.com/SocialSisterYi/bilibili-API-collect/blob/master/danmaku/danmaku.md教程
def get_cid(bv='1Lt411m7iJ'):  # 调用api获取指定bv的cid  63369190
    # http://api.bilibili.com/x/web-interface/view?avid={AV 号}
    url='http://api.bilibili.com/x/web-interface/view?bvid='+bv
    print(url)
    response=requests.get(url).text
    mydict=json.loads(response)
    data=mydict['data']['pages']  # 得到cid存放的列表，元素是字典，cid是字典的键
    cid_list=[]
    for i in data:
        cid_list.append(i['cid'])
    print(cid_list)
get_cid()


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
    print(related_attributes)
    print(barrages)
get_danmu()