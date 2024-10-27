import tkinter as tk
import tkinter.font as tf

def transtale_result(strs):
    import requests
    url='http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3756.400 QQBrowser/10.5.4039.400'}
    data={
        'i': strs,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }
    response=requests.post(url,data,headers=headers)
    result=response.json()['translateResult'][0][0]
    return str(result.get('tgt'))

def get_weather_information(city):
    import requests
    import re
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    data={
    'cityname': city,
    'callback': 'success_jsonpCallback',
    '_': '1586315159350'
    }
    url='http://toy1.weather.com.cn/search?'
    response1=requests.get(url,params=data,headers=headers).text
    number=re.findall('"ref":"(\d*?)~',response1)[0]
    weather_url='http://www.weather.com.cn/weather1d/'+number+'.shtml#input'
    response2=requests.get(weather_url,headers=headers).content.decode('utf-8')
    seven_daysdata=re.findall('id="hidden_title" value="(.*?)"',response2)[0].split()
    return ' '.join(seven_daysdata)

window = tk.Tk()
window.title('My Window')
window.geometry('900x600')
font =tf.Font(family='楷体', size=12)
##########################################翻译框架#################################################
def insert_result1():
    result1.delete(1.0, tk.END)#删除内容
    strs = data1.get('0.0', 'end')
    var=transtale_result(strs)
    result1.insert('insert',var)

frame1=tk.Frame(window,height=1)
frame1.place(x=0,y=30)
#建立输入输出框
frame3=tk.Frame(window,height=1)
frame3.place(x=0,y=0)
l1 = tk.Label(frame3, text='请输入需要翻译的内容：', font=font, width=22, height=1)
l1.pack(side='left')
data1 = tk.Text(frame1, width=50,height=10, font=font)
data1.pack(side='left',fill='y')
result1 = tk.Text(frame1, width=50,font=font)
result1.pack(side='right',fill='y')
b1 = tk.Button(frame1, text='点击翻译',height=3,command=insert_result1,font=font)
b1.pack(side='left')
##########################################天气查询框架#################################################
var2 = tk.StringVar()
def insert_result2():
    strs = data2.get()
    data=get_weather_information(strs)
    var2.set(data)

frame2=tk.Frame(window,height=10)
frame2.place(x=20,y=430)
l2 = tk.Label(frame2, text='请输入需要城市名：', font=font, width=14, height=2)
l2.pack(side='left')
data2 = tk.Entry(frame2, font=('楷体',14))
data2.pack(side='left')
result2 = tk.Entry(frame2, textvariable=var2,width=40,font=('楷体',14))
result2.pack(side='right')
b2 = tk.Button(frame2, text='点击查询天气信息',height=3,command=insert_result2,font=font)
b2.pack(side='left')





window.mainloop()
