import pandas as pd
#pd.Series(data可迭代对象或者字典,index不写默认为0123..,dtype=指定数据产生时的类型,name指定列索引,copy=False)
#产生两列数据，第一列是键，第二列是值，本质就是左右两列键值对对应起来

###创建Series对象、索引
s1=pd.Series([11,57,12,25,32],index=list('abcde'))
print(s1.keys())  # 得到index，即键
print(s1.values)  # 得到值
print(s1['a'])  # 索引
print(s1[:2])  # 同时支持类似列表操作的切片
print(s1[0])  # 通过下标来索引，但是当创建时的index为数字，则变成了键值对，如下
print(s1[s1>20])  # 得到大于20的几个数,但是不支持左右一起，例如print(s1[20<s1<40])
'''
s2=pd.Series(list('我爱张瑞龙'),index=[1,2,3,4,5])
print(s2[1])  # 得到  '我'
print(s2[0])  # 会报错
'''
###修改、删除原数据
s1['a']='你'  # 通过类似字典键值对更新的方式
s1.replace('我','你')  # 把 '我' 替换成 '你'
s1.pop('a')  # 通过index删除对应的值,会弹出。t=s1.pop('a')这样写就不会弹出了
del(s1['s'])  # 通过index删除对应的值,不会弹出