import xlwt       #导入xlwt模块
import xlrd       #导入xlrd模块
from xlutils.copy import copy       #导入import模块的copy函数，接下来就可以直接使用函数copy了。

fileName = "E:\\4.xls"
sheetName = "sheet1"

styleBoldRed = xlwt.easyxf('font: color-index red, bold on')   #设置字体，颜色为红色，加粗
oldWb = xlrd.open_workbook(fileName, formatting_info=True)   #使用xlrd.open_workbook函数打开文件，formatting_info=True表示保留该文件的格式
newWb = copy(oldWb)   #通过copy函数把oldWb copy到newWb，然后通过编辑newWb来实现编辑已经存在的文件。
newWs = newWb.get_sheet(0)   #读取第一个sheet
newWs.write(4, 0, "value1",styleBoldRed)    #第5行第1列写入值“value1”，格式采用styleBoldRed。
newWs.write(4, 1, "value2",styleBoldRed)   #第5行第2列写入值“value2”
newWs.write(4, 2, "value3",styleBoldRed)   #第5行第3列写入值“value3”
newWb.save(fileName)   #文件保存为"E:\\4.xls"