'''
QLabel控件
setAlignment()：设置文本的对齐方式
setIndent()：设置文本缩进
text()：获取文本内容
setBuddy()：设置伙伴关系
setText()：设置文本内容
selectedText()：返回所选择的字符
setWordWrap()：设置是否允许换行
QLabel常用的信号（事件）：
1.  当鼠标滑过QLabel控件时触发：linkHovered
2.  当鼠标单击QLabel控件时触发：linkActivated
'''
import sys
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette  # QPalette是调色板，用来设置背景色  QPixmap类来创建图片标签
from PyQt5.QtCore import Qt


class QLabelDemo(QWidget) :
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)  # 创建背景
        palette = QPalette()  # 创建调色板
        palette.setColor(QPalette.Window, Qt.blue)  # 设置背景色
        label1.setPalette(palette)  # 对Label使用调色板
        label1.setAlignment(Qt.AlignCenter)  # 设置居中对齐

        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./images/python.jpg"))  # QPixmap类来创建图片标签

        # 如果设为True，用浏览器打开网页，如果设为False，调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")  # 设置文本和超链接
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接')

        # 创建垂直布局，并将控件放进去
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)

        label2.linkHovered.connect(self.linkHovered)  # 对label2设置划过的槽
        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')

    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())