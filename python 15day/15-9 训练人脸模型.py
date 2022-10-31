import os
import cv2
from PIL import Image
import numpy as np

def getImageAndLabels(path):
    facesSamples=[]
    ids=[]
    #所有样本的图像
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    #检测人脸
    face_detector = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_alt2.xml')
    #打印数组imagePaths
    print('数据排列：',imagePaths)
    #遍历列表中的图片
    for imagePath in imagePaths:
        #打开图片,黑白化 cvtColor BGR2GRAY
        PIL_img=Image.open(imagePath).convert('L')
        #将图像转换为数组，以黑白深浅
       # PIL_img = cv2.resize(PIL_img, dsize=(400, 400))

        #np.array 图片变成矩阵数组
        img_numpy=np.array(PIL_img,'uint8')
        #获取图片人脸特征
        faces = face_detector.detectMultiScale(img_numpy)
        #获取每张图片的id和姓名  1.shen.jpg 2.shen.jpg
        id = int(os.path.split(imagePath)[1].split('.')[0])
        #预防无面容照片
        for x,y,w,h in faces:
            ids.append(id)
            facesSamples.append(img_numpy[y:y+h,x:x+w])
        #打印脸部特征和id
        #print('fs:', facesSamples)
        print('id:', id)
        #print('fs:', facesSamples[id])
    print('fs:', facesSamples)
    #print('脸部例子：',facesSamples[0])
    #print('身份信息：',ids[0])
    return facesSamples,ids

if __name__ == '__main__':
    #图片路径
    path='./data/train/'
    #获取图像数组和id标签数组和姓名
    faces,ids=getImageAndLabels(path)
    #获取训练对象
    recognizer=cv2.face.LBPHFaceRecognizer_create()
    #recognizer.train(faces,names)#np.array(ids)
    #训练模型
    recognizer.train(faces,np.array(ids))
    #保存文件
    #trainer.yml训练结果。
    recognizer.write('trainer/trainer.yml')
    #save_to_file('names.txt',names)