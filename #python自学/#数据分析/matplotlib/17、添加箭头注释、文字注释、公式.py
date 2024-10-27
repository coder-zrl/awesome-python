import numpy as np
import matplotlib.pyplot as plt
import matplotlib; matplotlib.use('TkAgg')
# from matplotlib import font_manager
# # 中文字体准备
# my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/msyh.ttc")  # 设置字体为微软雅黑
# plt.xticks(barrage_type, fontproperties=my_font)

# 注释
x = np.arange(-10,11,1)
y = x*x
plt.plot(x,y)
plt.annotate('This is the bottom',xy=(0,1),xytext=(0,20),
             arrowprops=dict(facecolor='r',headlength=10,headwidth=20,width=10))
# 'This is the bottom'是注释信息，xy是箭头坐标，xytext是这一行字的起始坐标
# arrowprops定义注释的形状,headlength表示箭头的长度，headwidth剪头的宽度，width长方形部分的宽度
plt.show()

#文字
x = np.arange(-10,11,1)
y = x*x
plt.plot(x,y)
# family 字体  style=normal/italic斜体  weight 字体粗细
plt.text(-2,40,'function:y=x*x',family='serif',size=20,color='r',
         style='italic',weight='bold',bbox=dict(facecolor='r',alpha=0.2))
# family表示字体fantasy这个好看，size字号，color颜色，style为斜体，normal为正常，weight为粗体，写成数字也行0-1000
# bbox外面画一个框框，alpha透明度0.2
plt.show()


# tex公式
# 自带Tex引擎，以$符号为开头和结尾
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([1, 7])
ax.set_ylim([1, 5])
ax.text(2, 4, r"$\alpha_i \beta_i \pi \lambda \omega$", size=20)
ax.text(4, 4, r"$\sin(0)=\cos(\frac{\pi}{2})$", size=20)
ax.text(2, 2, r"$\lim_{x \rightarrow y}\frac{1}{x^3}$", size=20)
ax.text(4, 2, r"$\sqrt[4]{x}=\sqrt{y}$", size=20)
plt.show()