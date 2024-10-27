#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
这个例子显示了一个进度条控件。
self.pbar = QProgressBar(self) //进度条的定义
self.pbar.setGeometry(30, 60, 100, 30) //进度条的大小和位置，前两个是位置，后两个是大小
进度条默认一般是长度为100，步长度一般使用一个变量来控制，这个变量要初始化为零，需要清空的时候要记得清零：
self.step = 0
当步长设置的的时候，一定要设置到进度条的属性里面，不然的话意义不大，如下所示：
self.step = self.step+1
self.pbar.setValue(self.step)
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QProgressBar, QPushButton
from PyQt5.QtCore import QBasicTimer

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)
        self.timer = QBasicTimer()
        self.step = 0

        self.btn = QPushButton('开始', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('进度条')
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.step = 0
            self.pbar.setValue(self.step)
            self.timer.stop()
            self.btn.setText('完成')
            return
        self.step = self.step+1
        self.pbar.setValue(self.step)

    def doAction(self, value):
        print("do action")
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('开始')
        else:
            self.timer.start(100, self)
            self.btn.setText('停止')

if __name__ == '__main__':
     app = QApplication(sys.argv)
     ex = Example()
     sys.exit(app.exec_())