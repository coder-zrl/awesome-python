import xlrd
excel = xlrd.open_workbook("2020-06-10 已配送.xls")
sheet = excel.sheet_by_index(0) #通过索引读取sheet对象，第一个sheet的索引为"0"
row_the_first = sheet.row_values(0) #读取第1行的所有数据，并以列表的形式存储到row_3中
all_cell_data={}
for i in range(len(row_the_first)):  # 第几列
    one_col_data=sheet.col_values(i)[1:]  # 没有信息的会变成''
    all_cell_data[row_the_first[i]]=one_col_data
print(all_cell_data)

def read_excel(path):
    import xlrd
    excel = xlrd.open_workbook(path)
    sheet = excel.sheet_by_index(0)  # 通过索引读取sheet对象，第一个sheet的索引为"0"
    row_the_first = sheet.row_values(0)  # 读取第1行的所有数据，并以列表的形式存储到row_3中
    all_cell_data = {}
    for i in range(len(row_the_first)):  # 第几列
        one_col_data = sheet.col_values(i)[1:]  # 没有信息的会变成''
        all_cell_data[row_the_first[i]] = one_col_data
    return all_cell_data