import cv2 as cv

img = cv.imread('./img/test1.jpg')
x,y,w,h = 0,0,200,200
#rectangle 矩形
#参数1：图像
#参数2：左上角坐标，右下角坐标
#参数3: 颜色 B G R
#参数4：矩形线的宽度
cv.rectangle(img,(x,y,x+w,y+h),color=(0,0,255),thickness=2)
#circle 圆形
#参数1：图像
#参数2：圆心坐标 (只能是整数)
#参数3: 半径
#参数4：颜色
#参数5：圆形线的宽度
cv.circle(img,center=((x+w)//2,(y+h)//2),radius=100,color=(255,0,0),thickness=2)
# putText 文本
#FONT_HERSHEY_SIMPLEX 文本格式
font=cv.FONT_HERSHEY_SIMPLEX
#参数1：图像
#参数2：文本内容（只能用英文）
#参数3: 文本的左下角坐标
#参数4：文本格式
#参数5：字体大小
#参数6：文本颜色
#参数7：粗细
cv.putText(img,'guanxi',(100,100),font,1,(255,255,255),2)

cv.imshow('img',img)
cv.waitKey(0)
cv.destroyAllWindows()
