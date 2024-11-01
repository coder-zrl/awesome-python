import sys

#必须使用两个类：QApplication和QWidget。都在PyQt5.QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget
# 主窗口类型有3种窗口
# QMainWindow：可以包含菜单栏、工具栏、状态栏和标题栏，是最常见的窗口形式
# QDialog：是对话窗口的基类。没有菜单栏、工具栏、状态栏。
# QWidget：不确定窗口的用途，就使用QWidget。






if __name__ == '__main__':
    # 创建QApplication类的实例
    app = QApplication(sys.argv)
    # 创建一个窗口
    w = QWidget()
    # 设置窗口的尺寸
    w.resize(400,200)
    # 移动窗口
    w.move(300,300)
    # 设置窗口的标题
    w.setWindowTitle('第一个基于PyQt5的桌面应用')
    # 显示窗口
    w.show()

    # 进入程序的主循环、并通过exit函数确保主循环安全结束
    sys.exit(app.exec_())
