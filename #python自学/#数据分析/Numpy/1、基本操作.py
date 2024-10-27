import numpy as np

# 创建数组
t1 = np.array([1, 2, 3])
print(t1,type(t1))

t2 = np.array(range(10))
print(t2,type(t2))

t3 = np.arange(4,10,2)  #用法同range
print(t3,type(t3))

# 查看数据类型
print(t3.dtype)

# 创建指定数据类型
t4 = np.array(range(10), dtype="int64")
print( t4)
print(t4.dtype)

# 调整数据类型
t5 = t4.astype("bool")
print(t5)
print(t5.dtype)

# numpy取小数
import random as rd
randArray = np.array([rd.random() for i in range(6)])
print(randArray)

roundedRandArray = np.round(randArray, 2)
print(roundedRandArray)


