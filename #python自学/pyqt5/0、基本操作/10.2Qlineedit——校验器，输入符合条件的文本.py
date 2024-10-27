'''
现在QLineEdit控件的输入（校验器）
如限制只能输入整数、浮点数或满足一定条件的字符串
'''

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator, QRegExpValidator
# QIntValidator为只能输入整数，QDoubleValidator输入浮点数，QRegExpValidator符合正则表达式的
from PyQt5.QtCore import QRegExp
# 引入正则表达式的类
import sys


# 综合案例有更简单的设置方式
class QLineEditValidator(QWidget):
    def __init__(self):
        super(QLineEditValidator,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('校验器')

        # 创建表单布局
        formLayout = QFormLayout()

        intLineEdit = QLineEdit()
        doubleLineEdit = QLineEdit()
        validatorLineEdit = QLineEdit()

        formLayout.addRow('整数类型', intLineEdit)
        formLayout.addRow('浮点类型', doubleLineEdit)
        formLayout.addRow('数字和字母',validatorLineEdit)

        intLineEdit.setPlaceholderText('整型')
        doubleLineEdit.setPlaceholderText('浮点型')
        validatorLineEdit.setPlaceholderText('字母和数字')

        ################### 综合案例有更简单的设置方式 ########################
        # 整数校验器 [1,99]
        intValidator = QIntValidator(self)  # 加self是把QLineEditValidator对象作为参数传给QIntValidator
        intValidator.setRange(1,99)

        # 浮点校验器 [-360,360]，精度：小数点后2位
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360,360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)  # 正常地显示浮点数，没啥用？
        # 设置精度，小数点2位
        doubleValidator.setDecimals(2)

        # 字符和数字
        reg = QRegExp('[a-zA-Z0-9]+$')
        validator = QRegExpValidator(self)
        validator.setRegExp(reg)

        # 设置校验器

        intLineEdit.setValidator(intValidator)
        doubleLineEdit.setValidator(doubleValidator)
        validatorLineEdit.setValidator(validator)

        self.setLayout(formLayout)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLineEditValidator()
    main.show()
    sys.exit(app.exec_())