import cv2


face_cascade = \
    cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_default.xml')
#VideoCapture 电脑中摄像头设备
#VideoCapture(设备序号)
cap = cv2.VideoCapture(0)

n = 0
#判断摄像头是否打开
while cap.isOpened():
    #读取摄像头的每一帧图像
    flag,frame = cap.read()


    #灰度化
    gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, 1.3, 5)

    #temp 储存了识别之前的图片
    temp = frame.copy()
    #人脸检测
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    cv2.imshow('cap', frame)


    #关闭摄像头（关闭整个循环）
    #cv2.waitKey(1) 获取键盘编码(数字)
    keCode = cv2.waitKey(1)
    if keCode == ord('q'):
        break
    elif keCode == ord('s'):
        cv2.imwrite('./data/train/'+str(n)+'.shen.jpg',temp)
        n += 1
#摄像头释放
cap.release()

cv2.destroyAllWindows()
