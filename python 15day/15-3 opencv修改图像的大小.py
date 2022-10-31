import cv2 as cv

gray = cv.imread('./img/test1_gray.jpg')
resize_img = cv.resize(gray,dsize=(128,128))
cv.imshow('gray',gray)
cv.imshow('resize',resize_img)

cv.waitKey(0)
cv.destroyAllWindows()