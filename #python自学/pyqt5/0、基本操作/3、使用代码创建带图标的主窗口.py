import sys
from PyQt5.QtWidgets import QMainWindow,QApplication
from PyQt5.QtGui import QIcon#设置图标


class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin,self).__init__()

        # 设置主窗口的标题
        self.setWindowTitle('第一个主窗口应用')
        # 设置窗口的尺寸
        self.resize(400,300)
        #设置状态栏
        self.status = self.statusBar()
        self.status.showMessage('只存在5秒的消息',5000)#状态栏的消息，停留5000毫秒，即5秒

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon('./images/Dragon.ico'))#添加图标
    main = FirstMainWin()
    main.show()
    sys.exit(app.exec_())