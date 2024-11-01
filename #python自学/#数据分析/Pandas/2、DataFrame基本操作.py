import pandas as pd
#df=pd.DataFrame(data常为字典类型数据,index=None,columns=None,dtype=None,copy=False)

###创建DataFrame对象
# 字典-->方式一
data={'姓名':['龙','浩','狗屎'],'电话':[10086,10010,10011],'性别':['男','女','未知']}
df=pd.DataFrame(data,columns=['电话','姓名','性别'])  # 因为字典是无序的，有时可能需要通过限制columns来确保列的顺序
print(df)
# 字典-->方式二
data=[{'姓名':'龙','电话':10086,'性别':'男'},{'姓名':'浩','电话':10010,'性别':'女'},{'姓名':'狗屎','电话':10011,'性别':'未知'}]
df=pd.DataFrame(data,columns=['电话','姓名','性别'])  # 因为字典是无序的，有时可能需要通过限制columns来确保列的顺序
print(df)  # 创建完毕
# 可迭代对象-->方式三
data=[[10086,'龙','男'],[10010,'浩','女'],[10011,'狗屎','未知']]  # 竖着对应的，即每个小列表应该是一条信息
df=pd.DataFrame(data,columns=['电话','姓名','性别'])  # 因为字典是无序的，有时可能需要通过限制columns来确保列的顺序
print(df)  # 创建完毕

###DataFrame的读取
print(df['电话'])  # 读取一列，返回df对象  ！！！list(df['电话'])得到的是[10086, 10010, 10011]
print(df[['电话','性别']])  # 读取多列，返回df对象  ！！！list(df[['电话','性别']])得到的是['电话', '性别']

