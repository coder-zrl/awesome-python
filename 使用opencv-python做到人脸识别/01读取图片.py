import cv2 as cv
#读取图片
img=cv.imread('C:\\Users\\86166\\Desktop\\q.png') #添加路径要写两个\\
#显示图片
cv.imshow('title',img)
#等待键盘输入，0默认为无限时长，单位为毫秒
cv.waitKey(0)
#空间释放  由于底层是c++编写的
cv.destroyAllWindows()
