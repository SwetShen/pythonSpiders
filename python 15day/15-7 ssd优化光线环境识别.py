import cv2

#.h5  .caffemodel 都需要训练生成
model_file = "dnn_face_detector/res10_300x300_ssd_iter_140000_fp16.caffemodel"
config_file = "dnn_face_detector/deploy.prototxt"
# readNetFromCaffe 读取.caffemodel模型
net = cv2.dnn.readNetFromCaffe(config_file,model_file)
# 90% 百分比 ：当人脸的概率大于90的时候，就是一张人脸。
threshold = 0.9

img = cv2.imread('./img/test2.jpg')
#img.shape 图片的形状大小
frameHeight = img.shape[0]
frameWidth = img.shape[1]

#blob(二进制文件)FromImage
#参数1：图像
#参数2：通道的缩放比例（R、G、B）
#参数3：面部轮廓的检测大小
#参数4：[104,117,123] 暗光条件下，可以识别
#参数5，6： 默认的裁剪方式和图像深度
blob = cv2.dnn.blobFromImage(img,1.0,(300,300),[104,117,123],False,False)

#设置输入的格式
net.setInput(blob)
# forward 前向传播 识别出人脸的结果
detections = net.forward()

# 遍历识别的人脸结果
for i in range(detections.shape[2]):
    # 人脸参数的得分
    detection_score = detections[0,0,i,2]
    #超过90%拟合度，就是人脸。
    if detection_score > threshold:
        #图像的左上角坐标和右下角坐标
        x1 = int(detections[0,0,i,3]*frameWidth)
        y1 = int(detections[0,0,i,4]*frameHeight)
        x2 = int(detections[0,0,i,5]*frameWidth)
        y2 = int(detections[0,0,i,6]*frameHeight)
        #绘制矩形
        cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,0),2)
cv2.imwrite('./img/test2_ssd_detect.jpg',img)