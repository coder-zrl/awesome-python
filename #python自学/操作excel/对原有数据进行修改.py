from xlutils.copy import copy
import xlrd
#xlutils:修改excel
book1 = xlrd.open_workbook('stu.xls')
book2 = copy(book1)#拷贝一份原来的excel
# print(dir(book2))
sheet = book2.get_sheet(0)#获取第几个sheet页，book2现在的是xlutils里的方法，不是xlrd的
sheet.write(1,3,0)
sheet.write(1,0,'hello')
book2.save('stu.xls')