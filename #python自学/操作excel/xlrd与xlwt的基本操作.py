#xlrd读excel：
import xlrd
book = xlrd.open_workbook('data.xlsx')
sheet1 = book.sheets()[0]
nrows = sheet1.nrows
print('表格总行数',nrows)
cell_3_3 = sheet1.cell(2,2).value
print('第3行第3列的单元格的值：',cell_3_3)
ncols = sheet1.ncols
print('表格总列数',ncols)
row3_values = sheet1.row_values(2)
print('第3行值',row3_values)
col3_values = sheet1.col_values(2)
print('第3列值',col3_values)

#xlwt写excel
import xlwt
workbook = xlwt.Workbook()
worksheet = workbook.add_sheet('test')
worksheet.col(0).width = 4444   #第一列宽度
worksheet.write(0,0,'A1data')
worksheet.write_merge(0, 1, 6, 7,'源码')   #合并第1行到第二行的  第7和8列。后面是合并后写什么内容，如果合并本行的，前两个参数就写一样的

workbook.save('excelwrite.xls')