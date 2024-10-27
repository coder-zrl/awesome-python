import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
with open('XRD_AFO.txt', 'r',encoding='utf-8') as data:
    ls = [x.strip().split() for x in data]
    lsx = [float(x[0]) for x in ls]
    lsy = [float(x[1]) for x in ls]
    plt.plot(lsx, lsy, color='green')
    newy=[4000]*len(lsx)
    newy2=[6000]*len(lsx)
    plt.plot(lsx, newy,'--r')
    plt.plot(lsx, newy2,'-b')
    plt.xlabel('2d')
    plt.ylabel('Intensity')
    plt.title('X射线衍射图谱')
    plt.show()