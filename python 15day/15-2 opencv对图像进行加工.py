import cv2 as cv

img = cv.imread('./img/test1.jpg')
#将图片灰度化  2 = to
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray_img',gray_img)

#保存处理好的图片
cv.imwrite('./img/test1_gray.jpg',gray_img)

cv.waitKey(0)
cv.destroyAllWindows()