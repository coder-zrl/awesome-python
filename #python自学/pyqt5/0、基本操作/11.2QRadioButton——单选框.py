'''

单选按钮控件（QRadioButton）

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo,self).__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('QRadioButton')
        layout = QHBoxLayout()
        self.button1 = QRadioButton('单选按钮1')
        self.button1.setChecked(True)  # 设置为默认选中状态

        self.button1.toggled.connect(self.buttonState)  # toggled是状态切换的信号
        layout.addWidget(self.button1)

        self.button2 = QRadioButton('单选按钮2')
        self.button2.toggled.connect(self.buttonState)
        layout.addWidget(self.button2)
        self.setLayout(layout)


    def buttonState(self):
        radioButton = self.sender()  # 把对象传给radioButton变量，就不用使用lambda表达式了
        #if radioButton.text()=='单选按钮1'
        if radioButton.isChecked() == True:
            print('<' + radioButton.text() + '> 被选中')
        else:
            print('<' + radioButton.text() + '> 被取消选中状态')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QRadioButtonDemo()
    main.show()
    sys.exit(app.exec_())