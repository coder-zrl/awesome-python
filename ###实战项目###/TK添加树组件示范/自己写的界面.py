from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import requests
import re

def show_data():
    global data_dict
    the_tpye=value1.get()
    the_year=2019-eval(value2.get()[:-1])
    for i in data_dict:
        if i ==the_tpye:
            tkinter.messagebox.showinfo(title='Hi', message='%s年%s的数据为%s亿元'%(value2.get(),value1.get()[:-4],data_dict[i][the_year]))



def spyder():
    global data_dict
    url = 'http://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=hgnd&rowcode=zb&colcode=sj&wds=%5B%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0201%22%7D%5D&k1=1592276489221&h=1'
    response = requests.get(url).content.decode()
    data_list = re.findall('"strdata":"(.*?)"}?', response)
    data_dict = {'国民总收入(亿元)': data_list[0:10], '国内生产总值(亿元)': data_list[10:20], '第一产业增加值(亿元)': data_list[20:30],
                 '第二产业增加值(亿元)': data_list[30:40], '第三产业增加值(亿元)': data_list[40:50], '人均国内生产总值(元)': data_list[50:60]}
    for i in data_dict:
        tv.insert('', 'end', values=[i]+data_dict[i])


data_dict={}
win = Tk()
win.title("国内生产总值查询工具")
win.geometry('730x400')

lb1 = Label(win, text="指标类型", font=('tahoma 12 normal', 10))
lb1.grid(column=0, row=2)
lb2 = Label(win, text="查询年份", font=('tahoma 12 normal', 10))
lb2.grid(column=0, row=4)

b1 = Button(win, text='点击爬取信息',font=('tahoma 12 normal', 10),height=2, command=spyder)
b1.grid(column=0, row=1)
b2 = Button(win, text='点击查询',font=('tahoma 12 normal', 10),height=2, command=show_data)
b2.grid(column=0, row=6)


# Define tkinter data type
value1 = StringVar()
cbx_1 = ttk.Combobox(win, width=16, height=8, textvariable=value1)
cbx_1.grid(column=0, row=3)
cbx_1["values"] = ['国民总收入(亿元)','国内生产总值(亿元)','第一产业增加值(亿元)','第二产业增加值(亿元)','第三产业增加值(亿元)','人均国内生产总值(元)']
cbx_1.current(0)

value2 = StringVar()
cbx_2 = ttk.Combobox(win, width=16, height=8,textvariable=value2)
cbx_2.grid(column=0, row=5)
cbx_2["values"] = ["2019年","2018年","2017年","2016年","2015年","2014年","2013年","2012年","2011年","2010年"]
cbx_2.current(0)


area = ('指标', "2019年","2018年","2017年","2016年","2015年","2014年","2013年","2012年","2011年","2010年")
ac=('指标', "2019年","2018年","2017年","2016年","2015年","2014年","2013年","2012年","2011年","2010年")
dc=('指标', "2019年","2018年","2017年","2016年","2015年","2014年","2013年","2012年","2011年","2010年")
tv = ttk.Treeview(win, columns=ac, show='headings',height=7, displaycolumns=dc)
tv.column(ac[0], width=130, anchor='c')
tv.heading(ac[0], text='指标')
for i in range(1,11):
    tv.column(ac[i], width=60, anchor='c')
    tv.heading(ac[i], text=area[i])
tv.grid(column=0, row=7)

win.mainloop()