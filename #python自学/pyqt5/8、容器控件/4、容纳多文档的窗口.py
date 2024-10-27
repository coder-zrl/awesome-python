'''

容纳多文档的窗口

QMdiArea

QMdiSubWindow

'''

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class MultiWindows(QMainWindow):
    count = 0  # 记录一下多少个窗口

    def __init__(self, parent=None):
        super(MultiWindows, self).__init__(parent)

        self.setWindowTitle("容纳多文档的窗口")

        self.mdi = QMdiArea()  # 创建一个容纳多文档的对象
        self.setCentralWidget(self.mdi)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        file.addAction("cascade")  # 层叠方式
        file.addAction("Tiled")  # 平铺方式

        file.triggered.connect(self.windowaction)
    def windowaction(self,q):
        print(q.text())  # 当前的文本
        if q.text() == "New":
            MultiWindows.count = MultiWindows.count + 1
            sub = QMdiSubWindow()
            sub.setWidget(QTextEdit())
            sub.setWindowTitle("子窗口" + str(MultiWindows.count))
            self.mdi.addSubWindow(sub)  # 把子窗口添加到mdi里
            sub.show()  # 显示这个窗口
        elif q.text() == "cascade":
            self.mdi.cascadeSubWindows()  # 层叠方式
        elif q.text() == "Tiled":
            self.mdi.tileSubWindows()  # 平铺方式



if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = MultiWindows()
    demo.show()
    sys.exit(app.exec_())