#图像处理库
import cv2 as cv

#img是opencv对象 （区别PIL的img对象）
img = cv.imread("./img/test1.jpg")
#imshow(图片署名，图片对象)
cv.imshow('real_img',img)

#让前面显示图片的操作停顿
cv.waitKey(0)
#图片退出浏览时关闭所有的窗口
cv.destroyAllWindows()