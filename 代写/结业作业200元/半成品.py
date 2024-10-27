import requests
import datetime
import xlwt
import re
import json
import sys
import matplotlib; matplotlib.use('TkAgg')
from matplotlib import font_manager
# 中文字体准备
my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")  # 设置字体为微软雅黑
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QMessageBox
from PyQt5.QtCore import QStringListModel,Qt
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon, QBrush, QColor,QStandardItemModel,QStandardItem


class GUI(QWidget):
    def __init__(self, arg=None):
        super(GUI, self).__init__(arg)
        # 设置初始大小与标题
        self.setWindowTitle('简易B站弹幕分析工具')
        self.resize(720, 600)
        self.setupUI()

    def setupUI(self):
        # 添加进度条
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(480,70,230,20)
        self.timer = QBasicTimer()
        self.step = 0

        # 添加BV号文本框和按钮
        self.bv_LineEdit = QLineEdit(self)
        self.bv_LineEdit.setPlaceholderText('请输入BV号')
        self.bv_LineEdit.setGeometry(480,30,100,30)
        self.get_barrages_button=QPushButton(self)
        self.get_barrages_button.setText('获取弹幕')
        self.get_barrages_button.setGeometry(600, 30, 80, 30)
        self.get_barrages_button.clicked.connect(self.get_barrages)

        # 显示弹幕信息
        self.tableview = QTableView(self)
        self.tableview.setGeometry(0,0,455,600)
        self.barrages, self.dates =[],[] # get_barrages()
        self.model = QStandardItemModel(len(self.barrages), 2)
        self.model.setHorizontalHeaderLabels(['弹幕内容', '发布时间'])
        for i in range(len(self.barrages)):  # 添加数据
            self.model.setItem(i, 0, QStandardItem(self.barrages[i]))
            self.model.setItem(i, 1, QStandardItem(self.dates[i]))
        self.tableview.setModel(self.model)  # 关联QTableView控件和Model
        self.tableview.setColumnWidth(0,350)

        # 高能进度条
        self.barrages_Progressbar_button=QPushButton(self)
        self.barrages_Progressbar_button.setText('生成高能进度条')
        self.barrages_Progressbar_button.setGeometry(480, 120, 120, 30)
        self.barrages_Progressbar_button.clicked.connect(self.creat_progress_png)

        # 弹幕Top10
        self.barrages_Top10_button=QPushButton(self)
        self.barrages_Top10_button.setText('生成弹幕Top10')
        self.barrages_Top10_button.setGeometry(480, 180, 120, 30)
        self.barrages_Top10_button.clicked.connect(self.creat_top10_png)

        # 弹幕类型分析
        self.barrages_type_button=QPushButton(self)
        self.barrages_type_button.setText('生成弹幕类型图')
        self.barrages_type_button.setGeometry(480, 240, 120, 30)
        self.barrages_type_button.clicked.connect(self.creat_type_png)

        # 弹幕颜色分析
        self.barrages_color_button=QPushButton(self)
        self.barrages_color_button.setText('生成弹幕颜色类型图')
        self.barrages_color_button.setGeometry(480, 300, 120, 30)
        self.barrages_color_button.clicked.connect(self.cerat_color_png)

        # 生成弹幕词云
        self.barrages_wordcloud_button=QPushButton(self)
        self.barrages_wordcloud_button.setText('生成弹幕词云')
        self.barrages_wordcloud_button.setGeometry(480, 360, 120, 30)
        self.barrages_wordcloud_button.clicked.connect(self.creat_wordcloud_png)

        # 保存为Excel
        self.barrages_wordcloud_button=QPushButton(self)
        self.barrages_wordcloud_button.setText('保存为Excel')
        self.barrages_wordcloud_button.setGeometry(480, 420, 120, 30)
        self.barrages_wordcloud_button.clicked.connect(self.save_excel)


    def updata_view(self):
        self.model = QStandardItemModel(len(self.barrages_list), 2)
        self.model.setHorizontalHeaderLabels(['弹幕内容', '发布时间'])
        # self.model.horizontalHeader().setVisible(False)
        for i in range(len(self.barrages_list)):  # 添加数据
            self.model.setItem(i, 0, QStandardItem(self.barrages_list[i]))
            self.model.setItem(i, 1, QStandardItem(self.sending_time[i]))
        self.tableview.setModel(self.model)  # 关联QTableView控件和Model
        self.tableview.setColumnWidth(0, 295)

    def get_barrages(self):
        self.get_barrages_button.setText('正在获取')
        bv_ccount=self.bv_LineEdit.text() if len(self.bv_LineEdit.text())!=0 else '1jW411Y7dL'
        url = 'http://api.bilibili.com/x/web-interface/view?bvid=' + bv_ccount
        print(url)
        response = requests.get(url).text
        if '请求错误' in response:
            QMessageBox.critical(self, '警告', '请输入正确的BV号', QMessageBox.Yes)
        else:
            mydict = json.loads(response)
            data = mydict['data']['pages']  # 得到cid存放的列表，元素是字典，cid是字典的键
            cid_list = []
            for i in data:
                cid_list.append(i['cid'])
        ###################################### 已经获取到cid_list ######################
        # 获取弹幕和相关属性
        # 弹幕列表
        self.barrages_list=[]
        # 弹幕在视频出现的时间，单位是秒
        self.barrage_sending_time = []
        # 弹幕类型，123普通，4底部，5顶部，6逆向，7精准定位，8代码位置，9BAS弹幕
        self.barrage_type = []
        # 弹幕字号，18小，25标准，36大
        self.barrage_size = []
        # 弹幕颜色，十进制RGB888值
        self.barrage_color = []
        # 弹幕发送时间，时间戳
        self.sending_time = []
        # 弹幕池类型 0普通池，1字幕池，2特殊池子（高级弹幕）
        self.barrage_pool_type = []
        # 返回HEX类型数据，用于屏蔽用户和查看用户发送的所有弹幕，也可反差用户ID
        self.encoded_users = []
        # 弹幕ID
        self.barrage_id = []
        for index,cid in enumerate(cid_list):
            self.step = (index+1)/len(cid_list)*100
            print(self.step)
            self.pbar.setValue(self.step)
            url = 'http://api.bilibili.com/x/v1/dm/list.so?oid=' + str(cid)
            print(url)
            response = requests.get(url).content.decode()  # 出现乱码问题，需要解码再重新编码
            related_attributes = re.findall('p="(.*?)"', response)  # 提取d标签p属性的内容
            barrages = re.findall('">(.*?)</d>?', response)  # 提取弹幕
            self.barrages_list+=barrages
            for related_attribute in related_attributes:
                one_barrage_of_data = related_attribute.split(',')
                self.barrage_sending_time.append(one_barrage_of_data[0])
                self.barrage_type.append(one_barrage_of_data[1])
                self.barrage_size.append(one_barrage_of_data[2])
                self.barrage_color.append(one_barrage_of_data[3])
                self.sending_time.append(one_barrage_of_data[4])
                self.barrage_pool_type.append(one_barrage_of_data[5])
                self.encoded_users.append(one_barrage_of_data[6])
                self.barrage_id.append(one_barrage_of_data[6])
        print(self.barrages_list)
        self.step = 0
        self.pbar.setValue(self.step)
        self.get_barrages_button.setText('获取弹幕')

        # 将时间戳变为现代时间
        self.change_time()
        print(self.sending_time)
        if len(self.barrages_list)==0:
            QMessageBox.critical(self,'警告','IP被限制未获取到弹幕内容',QMessageBox.Yes)
        else:
            QMessageBox.information(self, '消息', '共获取到'+str(len(self.barrages_list))+'条弹幕', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            self.updata_view()

    def creat_progress_png(self):
        def count(barrage_sending_time):
            mydict = {}
            for i in range(0, int(barrage_sending_time[-1]) + 1):
                for t in barrage_sending_time:
                    if i <= t <= i + 1:
                        mydict[i] = mydict.get(i, 0) + 1
            time = list(mydict.keys())
            frequency = (mydict.values())
            return time, frequency

        barrage_sending_time = self.barrage_sending_time
        barrage_sending_time = [eval(i) for i in barrage_sending_time]
        barrage_sending_time.sort()
        time, frequency = count(barrage_sending_time)
        plt.bar(x=time, height=frequency)
        plt.xticks(time, fontproperties=my_font)
        plt.title('高能进度条', fontproperties=my_font)
        plt.savefig("高能进度条.png", dpi=500, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
        plt.show()

    def creat_top10_png(self):
        def count(mylist):
            mydict = {}
            for i in mylist:
                mydict[i] = mydict.get(i, 0) + 1
            mylist = list(mydict.items())
            mylist.sort(key=lambda x: x[1], reverse=True)
            barrage = [i[0] for i in mylist[:10]]
            frequency = [i[1] for i in mylist[:10]]
            return barrage, frequency

        plt.figure(figsize=(16, 7))  # 设置图片初始化大小
        barrages = self.barrages_list
        barrage, frequency = count(barrages)
        plt.bar(x=barrage, height=frequency,color='#019899')
        plt.xticks(barrage, fontproperties=my_font)
        plt.title('弹幕Top10', fontproperties=my_font)
        plt.savefig("弹幕Top10.png", dpi=500, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
        plt.show()

    def creat_type_png(self):
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

        barrage_type = self.barrage_type
        if len(barrage_type)==0:
            QMessageBox.critical(self, '警告', '请先获取弹幕', QMessageBox.Yes)
        else:
            barrage_type, type_count = count(barrage_type)
            plt.bar(x=barrage_type, height=type_count)
            plt.xticks(barrage_type, fontproperties=my_font)
            plt.title('弹幕类型图',fontproperties=my_font)
            plt.savefig("弹幕类型图.png",dpi=500,bbox_inches = 'tight')  # 解决图片不清晰，不完整的问题
            plt.show()

    def cerat_color_png(self):
        def count(mylist):
            color_dict = {'16646914': '红色',
                          '16740868': '橘红',
                          '16755202': '橘黄',
                          '16765698': '淡黄',
                          '16776960': '黄色',
                          '10546688': '草绿',
                          '52480': '绿色',
                          '104601': '墨绿',
                          '4351678': '紫色',
                          '9022215': '青色',
                          '13369971': '品红',
                          '2236962': '黑色',
                          '10197915': '灰色',
                          '16777215': '白色'}
            mydict = {}
            for i in mylist:
                mydict[i] = mydict.get(i, 0) + 1
            for i in mydict.copy():
                try:
                    mydict[color_dict[i]] = mydict[i]
                    del mydict[i]
                except:
                    mydict['其他色'] = mydict.get(i, 0) + 1
                    del mydict[i]
            mylist = list(mydict.items())
            mylist.sort(key=lambda x: x[1], reverse=True)
            colors = [i[0] for i in mylist[:10]]
            frequency = [i[1] for i in mylist[:10]]
            return colors, frequency

        plt.figure(figsize=(12, 5))
        barrage_color = self.barrage_color
        colors, frequency = count(barrage_color)
        plt.bar(x=colors, height=frequency, width=0.3,color='#019899')
        plt.xticks(colors, fontproperties=my_font)
        plt.title('弹幕颜色类型图', fontproperties=my_font)
        plt.savefig("弹幕颜色类型图.png", dpi=500, bbox_inches='tight')  # 解决图片不清晰，不完整的问题
        plt.show()

    def creat_wordcloud_png(self):
        import jieba
        import wordcloud
        def count(barrages_list):
            lastlist = []
            for barrage in barrages_list:
                lastlist += jieba.lcut(barrage)
            laststr = ' '.join(lastlist)
            return laststr
        barrages = self.barrages_list
        laststr = count(barrages)
        w = wordcloud.WordCloud(width=2000, height=1000, font_path='msyh.ttc')
        w.generate(laststr)
        file_name = self.bv_LineEdit.text() if len(self.bv_LineEdit.text()) != 0 else '1jW411Y7dL'
        w.to_file(file_name+'.png')
        QMessageBox.information(self, '提示', '词云' + file_name + '.png' + '已保存', QMessageBox.Yes)
    def save_excel(self):
        workbook=xlwt.Workbook()
        worksheet=workbook.add_sheet('弹幕详情')
        for i in range(len(self.barrages_list)):
            worksheet.write(i, 0, self.barrages_list[i])
            worksheet.write(i, 1, self.sending_time[i])
        file_name=self.bv_LineEdit.text() if len(self.bv_LineEdit.text())!=0 else '1jW411Y7dL'
        workbook.save(file_name+'.xls')
        QMessageBox.information(self, '提示', 'Excel表格'+file_name+'.xls'+'已保存', QMessageBox.Yes)


    def change_time(self):
        nobaltime=[]
        for timeStamp in self.sending_time:
            dateArray = datetime.datetime.utcfromtimestamp(int(timeStamp))
            otherStyleTime = dateArray.strftime("%Y-%m-%d")
            nobaltime.append(otherStyleTime)
        self.sending_time=nobaltime



if __name__ == '__main__':
    app = QApplication(sys.argv)
    tree = GUI()
    tree.show()
    sys.exit(app.exec_())
