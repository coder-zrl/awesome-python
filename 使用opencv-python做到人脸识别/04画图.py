import cv2 as cv
img=cv.imread('q.jpg')
cv.imshow('title',img)

#矩形左上角坐标（x，y）矩形的宽度和高度是w，h
x,y,w,h=10,10,20,20
cv.rectangle(img,(x,y,x+w,y+h),color=(0,255,0),thickness=2)   #参数：①哪张图 ②矩形左上角坐标（x，y）右下角（x+w,y+h） ③颜色是BGR
cv.circle(img,center=(x+w//2,y+h//2),radius=15,color=(0,255,255),thickness=2)  #需要为整形参数

cv.imshow('title',img)




cv.waitKey(0)
cv.destroyAllWindows()