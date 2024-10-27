import sys
import MainwindowLayout#这个是pyulc生成的代码文件，放在同级目录
from PyQt5.QtWidgets import QApplication,QMainWindow

if __name__=='__main__':
    app=QApplication(sys.argv)#实例化对象
    mainwindow=QMainWindow()
    ui=MainwindowLayout.Ui_MainWindow()
    #向主窗口上添加控件
    ui.setupUi(mainwindow)
    mainwindow.show()
    sys.exit(app.exec_())