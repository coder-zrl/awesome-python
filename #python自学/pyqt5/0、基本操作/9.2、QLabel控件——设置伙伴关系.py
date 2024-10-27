'''
QLabel与伙伴控件
mainLayout.addWidget(控件对象,rowIndex,columnIndex,row,column)
'''


from PyQt5.QtWidgets import *
import sys


class QLabelBuddy(QDialog):  # QDialog是对话框类型窗口，是没有菜单的
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QLabel与伙伴控件')  # 创建标题

        nameLabel = QLabel('&Name',self)
        nameLineEdit = QLineEdit(self)
        # 设置伙伴控件
        nameLabel.setBuddy(nameLineEdit)
        passwordLabel = QLabel('&Password',self)
        passwordLineEdit = QLineEdit(self)
        # 连接伙伴控件
        passwordLabel.setBuddy(passwordLineEdit)

        btnOK = QPushButton('&OK')
        btnCancel = QPushButton('&Cancel')

        mainLayout = QGridLayout(self)  # 使用栅格化布局
        mainLayout.addWidget(nameLabel,0,0)  # 第一行第一列放置
        mainLayout.addWidget(nameLineEdit,0,1,1,2)  # 第一行第二列放置，占用一行两列

        mainLayout.addWidget(passwordLabel,1,0)
        mainLayout.addWidget(passwordLineEdit,1,1,1,2)

        mainLayout.addWidget(btnOK,2,1)
        mainLayout.addWidget(btnCancel,2,2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelBuddy()
    main.show()
    sys.exit(app.exec_())
