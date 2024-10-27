import wordcloud
def biaozhun():  # 添加字符和生成图片
    w=wordcloud.WordCloud()
    #w.generate(txt)向WordCloud对象w中加载文本txt
    w.generate("沃日你得啊啊啊啊啊啊")
    #w.to_file(filename) #将词云输出为图像文件,png或jpg格式
    w.to_file("outfile.png")
def qitacanshu():  # 其他参数
    w=wordcloud.WordCloud(width=600,height=400,
                          min_font_size=10,max_font_size=20,\
                          font_path='msyh.ttc',\
                          max_words=20,stop_words={'Python'},\
                          background_color='white'
                          )
    # width=600,height=400,设置图片大小
    # min_font_size=10,max_font_size=20,设置字体大小，最大最小
    # font_path='msyh.ttc',设置字体路径，这是微软雅黑
    # max_words=20,指定词云最多显示多少个词
    # stop_words={'Python'}，指定词云不显示的词
    # background_color='white'设置背景色为白色
    w.generate("Python and WordCloud")
    from scipy.misc import imread
    mk=imread('path')
    w=wordcloud.WordCloud(mask=mk)  #设置展示的形状

    w.to_file("outfile.png")
biaozhun()