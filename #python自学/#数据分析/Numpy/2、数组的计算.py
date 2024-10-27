import numpy as np

# shape查看多少行多少列   当是一维的时候得到的是个数
t1=np.array([[1,2,3],[4,5,6]])
print(t1.shape)  # 得到(2, 3)

# 三维数组
t2=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(t2.shape)

# reshape修改数组的形状,返回副本，参数是元组哦，一维写成reshape((长度,))，勿忘逗号
t4=np.arange(12)
t5=t4.resize((3,4))
print(t5)

# resize直接对原数组进行修改
t6=np.arange(12)
t6.resize((3,4))
print(t6)

# reshape为三维，第一个是块数，后面两个为二维的
t5=np.arange(24).reshape((2,3,4))
print(t5)

# 三维转一维
t5=np.arange(24).reshape((2,3,4))
t5=t5.reshape((24,))   # 不要写成(24,1)啊，那样会得到24个数组，每个都是一列，相当于拆成了24行，1列，
# 也别写成(1,24)，那样是二维的
print(t5)

# 多维转一维，以二维为例
t5=np.arange(12).reshape((3,4))
t5=t5.reshape((t5.shape[0]*t5.shape[1],))  # 行数乘列数得到总共几个元素
print(t5)

# 使用ravel直接压扁
t5=np.arange(12).reshape((3,4))
t5=t5.ravel()  # 行数乘列数得到总共几个元素
print(t5)

# 使用flatten转为一维
t5=np.arange(12).reshape((3,4))
t5=t5.flatten()  # 行数乘列数得到总共几个元素
print(t5)

# 简单加法  广播机制  加减乘除同理  # 除以0的话不会报错
t5=np.arange(12).reshape((3,4))
t5=t5+2  # 行数乘列数得到总共几个元素
print(t5)

# 矩阵加减乘除也是同理的
t5=np.arange(12).reshape((3,4))
t6=np.arange(12,24).reshape((3,4))
t5=t5+t6  # 行数乘列数得到总共几个元素
print(t5)

# 不同形状的矩阵进行计算，但是维度要相同，计算时会找对应的位置，如下，t5有3行，t4有4行，也能计算
t5=np.arange(12).reshape((3,4))
print(t5)
t6=np.arange(4).reshape((4,1))
t5=t5-t6  # 行数乘列数得到总共几个元素
print(t5)

