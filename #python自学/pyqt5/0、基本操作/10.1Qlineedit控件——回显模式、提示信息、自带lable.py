'''

QLineEdit控件与回显模式

基本功能：输入单行的文本

EchoMode（回显模式）

4种回显模式

1. Normal  #正常模式
2. NoEcho  #不显示（Linux命令行常用）
3. Password  #密码模式（即显示*）
4. PasswordEchoOnEdit  # 类似手机密码，开始会显示，离开后又变成了*


Mac : Command    Windows:Control
'''
from PyQt5.QtWidgets import *
import sys

class QLineEditEchoMode(QWidget) :
    def __init__(self):
        super(QLineEditEchoMode,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        #创建布局
        formLayout = QFormLayout()

        # 创建控件
        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        # 将控件添加到布局中，字符串是edit前面的名称
        formLayout.addRow("Normal",normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password",passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEdit",passwordEchoOnEditLineEdit)

        # placeholdertext  设置提示信息
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        # 设置显示模式
        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        # 在窗口放置布局
        self.setLayout(formLayout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditEchoMode()
    main.show()
    sys.exit(app.exec_())
