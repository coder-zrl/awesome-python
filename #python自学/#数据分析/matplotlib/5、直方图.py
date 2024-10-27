import numpy as np
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# 直方图
mu=100
sigma=20  # 标准差
x=mu+sigma*np.random.randn(2000)
print(list(x))
plt.hist(x,bins=10,color='red',density=True)  # bins表示生成多少列
# density=True会将纵坐标变成频率除以组距
plt.show()
