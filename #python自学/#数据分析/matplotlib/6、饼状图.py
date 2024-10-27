import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
# 饼状图
labels = 'A','B','C','D'
fracs = [15,30,45,10]
explode = [0,0,0.05,0]
plt.pie(x = fracs,labels = labels,autopct='%.1f%%',explode=explode,shadow=True)
# autopct='%.1f%%'表示显示每一块占的值
# explode表示对应的区域距离圆中心的距离
# shadow表示加上阴影
plt.show()
