import cv2 as cv

face_cascade = \
    cv.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')

eye_cascade = \
    cv.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

img = cv.imread('./img/test2.jpg')
gray_img = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray_img)

#使用级联检测器检测人脸
#参数1 图片
#参数2 图片遍历大小（1.3 原图的1.3倍）
#参数3 至少遍历的人脸个数
faces = face_cascade.detectMultiScale(gray_img,1.3,5)

#(x,y,w,h)
for (x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)

    print(x,y,w,h)
    #对眼睛的检测，基于已经识别到的人脸
    crop_img = gray_img[y:y+h,x:x+w]
    eyes = eye_cascade.detectMultiScale(crop_img)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(crop_img, (ex,ey),(ex+ew,ey+eh), color=(255, 0, 0), thickness=2)
        cv.imshow('detect', crop_img)


cv.waitKey(0)
cv.destroyAllWindows()

#Haar最大的问题，就是光照条件不好的时候，就会有问题。