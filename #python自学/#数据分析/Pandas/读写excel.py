#   读写 excel主要通过read_excel 、 to_excel函数实现，除了pandas还需要安装第三方库  xlrd、 openpyxl

import pandas as pd

#读取excel
df = pd.DataFrame(pd.read_excel('E:\\name.xlsx'))
print (df)

dft = pd.DataFrame([["王五",21],
                    ["赵六",32]],columns=['name','age'])
df = pd.concat([df,dft],ignore_index=True)
print(df)

#写入excel
df.to_excel('E:\\excel_to_python.xlsx', sheet_name='bluewhale_cc')

#写入Excel
writer = pd.ExcelWriter('E:\\output.xlsx')
df1 = pd.DataFrame(data={'col1':[1,1], 'col2':[2,2]})
print(df1)
df1.to_excel(writer,'Sheet12')
writer.save()