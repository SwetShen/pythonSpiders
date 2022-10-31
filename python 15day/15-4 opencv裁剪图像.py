#图像处理库
import cv2 as cv

img = cv.imread("./img/test1.jpg")

#裁剪图片
# img [x1:x2,y1:y2] 裁剪x1 y1到x2 y2的区域
crop_img = img[0:128,0:128]

cv.imshow('crop_img',crop_img)
cv.imshow('real_img',img)

#让前面显示图片的操作停顿
cv.waitKey(0)
#图片退出浏览时关闭所有的窗口
cv.destroyAllWindows()