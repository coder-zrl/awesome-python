#open-cv使用的是BGR三色通道，HSV分别表示色调、饱和度、黑暗程度
#灰度转化作用：降低计算量
import cv2 as cv
img=cv.imread('q.jpg')
cv.imshow('title',img)

#将图片灰度转化
gary_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gary_img',gary_img)

#保存图片
cv.imwrite('gary.jpg',gary_img)

cv.waitKey(0)
cv.destroyAllWindows()