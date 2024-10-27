# 显示控件提示消息
import sys
# QToolTip是提示信息的
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QToolTip,QPushButton,QWidget
from PyQt5.QtGui import QFont


class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Simsun',12))#设置提示信息的字体
        self.setToolTip('今天是<b>星期五</b>')#把鼠标放到界面一会就会显示提示信息
        self.setGeometry(300,30,200,300)
        self.setWindowTitle('设置控件提示消息')

        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮')
        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())
