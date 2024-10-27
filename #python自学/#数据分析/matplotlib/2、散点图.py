'''
查看相关性：正相关、负相关、不相关

'''

def demo1():  # 展示示范模型
    import matplotlib; matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    height=[161,170,182,175,173,165]
    weight=[50,58,80,70,69,55]
    plt.scatter(height,weight)
    plt.show()
def demo2():  # 展示不相关
    import numpy as np
    import matplotlib;matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    N=1000  # N表示样本容量
    x=np.random.randn(N)
    y=np.random.randn(N)
    plt.scatter(x,y)
    plt.show()

def demo3():  # 展示不相关
    import numpy as np
    import matplotlib;matplotlib.use('TkAgg')
    from matplotlib import pyplot as plt
    N=1000  # N表示样本容量
    x=np.random.randn(N)
    y=x+np.random.randn(N)*0.5  # 即y是由x生成的
    plt.scatter(x,y)
    '''
    外观调整  
    颜色:c='r'  红色
    点大小:s=20  面积的关系
    透明度:alpha=0.5  点多的地方颜色会变深  
    点形状:marker='o'  圆形吗，可以去官网查看
    '''
    plt.show()
demo1()
demo2()
demo3()