import cv2 as cv
img=cv.imread('q.jpg')
cv.imshow('title',img)
#查看原图形状
print('原图形尺寸',img.shape)

#修改图片尺寸
new_size_img=cv.resize(img,(140,40))  #分别是新图片长和宽的缩放，并不是裁剪
print(new_size_img.shape)

#保存图片
cv.imwrite('new_size_img.jpg',new_size_img)

#如果输入的是q时退出，因为运行cv.waitKey(0)时，键盘输入的会返回一个值
while True:
    if ord('q')==cv.waitKey(0):
        break
cv.destroyAllWindows()