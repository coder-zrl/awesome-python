import sys
from PyQt5.QtWidgets import QHBoxLayout,QMainWindow,QApplication,QPushButton,QWidget
# QHBoxLayout是水平布局的类，QPushButton是Button的类


class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle('退出应用程序')

        # 添加Button
        self.button1 = QPushButton('退出应用程序')
        # 将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()#创建水平布局
        layout.addWidget(self.button1)#将button加入到水平布局

        mainFrame = QWidget()
        mainFrame.setLayout(layout)

        self.setCentralWidget(mainFrame)#把主框架放在窗口上

    # 按钮单击事件的方法（自定义的槽）
    def onClick_Button(self):
        sender = self.sender()#获取对象
        print(sender.text() + ' 按钮被按下')
        app = QApplication.instance()
        # 退出应用程序
        app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())