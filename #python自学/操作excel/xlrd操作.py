import xlrd
excel = xlrd.open_workbook("data.xls")

sheet = excel.sheet_by_index(0) #通过索引读取sheet对象，第一个sheet的索引为"0"
row_3 = sheet.row_values(2) #读取第3行的所有数据，并以列表的形式存储到row_3中
col_3 = sheet.col_values(2) #读取第3列的所有数据，并以列表list的形式存储到col_3中
cell_12_7 = sheet.cell_value(11,6)   #读取第12行第7列的数据，并存储到cell_12_7中
cell_11_11 = sheet.cell(10,10).value #读取第11行第11列的数据，并存储到cell_11_11中
cell_7_8 = sheet.row(6)[7].value       #读取第7行第8列的数据
cell_8_7 = sheet.cel(7)[6].value        #读取第8列第7行的数据
num_rows = sheet.nrows             #读取sheet的总行数
num_cols = sheet.ncols               #读取sheet的总列数