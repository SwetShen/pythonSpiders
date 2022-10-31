import cv2

#VideoCapture 电脑中摄像头设备
#VideoCapture(设备序号)
cap = cv2.VideoCapture(0)

n = 0
#判断摄像头是否打开
while cap.isOpened():
    #读取摄像头的每一帧图像
    flag,frame = cap.read()
    cv2.imshow('cap',frame)

    #关闭摄像头（关闭整个循环）
    #cv2.waitKey(1) 获取键盘编码(数字)
    keCode = cv2.waitKey(1)
    if keCode == ord('q'):
        break
    elif keCode == ord('s'):
        cv2.imwrite('./data/train/'+str(n)+'.shen.jpg',frame)
        n += 1
#摄像头释放
cap.release()

cv2.destroyAllWindows()
