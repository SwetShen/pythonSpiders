import cv2
import os


#加载训练数据集文件
recogizer=cv2.face.LBPHFaceRecognizer_create()
recogizer.read('trainer/trainer.yml')

names=[]
warningtime = 0


#准备识别的图片
def face_detect_demo(img):
    # 转换为灰度图
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # haar检测识别器
    face_detector=cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
    # 识别灰度图的人像
    face=face_detector.detectMultiScale(gray,1.1,5,cv2.CASCADE_SCALE_IMAGE,(100,100),(300,300))
    #face=face_detector.detectMultiScale(gray)
    for x,y,w,h in face:
        #绘制矩形
        cv2.rectangle(img,(x,y),(x+w,y+h),color=(0,0,255),thickness=2)
        # lbp的算法器（yml文件）判断识别到的面部是否是我们特征集中人脸
        # ids 哪些图片被识别到了 confidence
        ids, confidence = recogizer.predict(gray[y:y + h, x:x + w])
        #print('标签id:',ids,'置信评分：', confidence)
        if confidence > 80:
            global warningtime
            warningtime += 1
            if warningtime > 100:
               # warning()
               warningtime = 0
            # 查无此人
            cv2.putText(img, 'unkonw', (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
        else:
            # 把这个人的姓名打出来
            cv2.putText(img,str(names[ids-1]), (x + 10, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 1)
    cv2.imshow('result',img)
    #print('bug:',ids)

def name():
    #将训练图片的名称放置到集合中
    path = './data/train/'
    #names = []
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    for imagePath in imagePaths:
       name = str(os.path.split(imagePath)[1].split('.',2)[1])
       names.append(name)


#摄像头
cap=cv2.VideoCapture(0)

name()
while True:
    flag,frame=cap.read()
    if not flag:
        break
    face_detect_demo(frame)
    if ord(' ') == cv2.waitKey(10):
        break
cv2.destroyAllWindows()
cap.release()
#print(names)