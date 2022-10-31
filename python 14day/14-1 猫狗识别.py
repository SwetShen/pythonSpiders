import os
import warnings
warnings.filterwarnings("ignore")
import tensorflow as tf
#ImageDataGenerator 图像容器（方便开发者使用卷积）
from keras.preprocessing.image import ImageDataGenerator
import keras
from keras import layers

#图像的主目录
base_dir = './cats_and_dogs/'
#训练图集'./cats_and_dogs/train'
train_dir = os.path.join(base_dir,'train')
#验证图集'./cats_and_dogs/validation'
validation_dir = os.path.join(base_dir,'validation')

#训练分类的猫狗数据集
train_cats_dir = os.path.join(train_dir,'cats')
train_dogs_dir = os.path.join(train_dir,'dogs')

validation_cats_dir = os.path.join(validation_dir,'cats')
validation_dogs_dir = os.path.join(validation_dir,'dogs')

#Dense 全连接层 在卷积神经网络中作为输出存在。
#Conv1D 一维卷积（复杂的线性回归）
#Conv2D 二维卷积（图像和文字）
#Conv3D 三维卷积（视频）

model = keras.Sequential()
#32 : filters 卷积核的数量
#(3,3) : 卷积核的大小为3x3
#activation ：激活函数
#input_shape ：图像的输入大小 和图层数量（图像深度）
model.add(layers.Conv2D(32,(3,3),activation='relu',input_shape=(64,64,3)))
# Pool 池化层
# MaxPool2D 最大池化
# (2,2) 我们将上一步的卷积中图像的宽高进行除2的操作（压缩）
model.add(layers.MaxPool2D(2,2))

model.add(layers.Conv2D(64,(3,3),activation='relu'))
model.add(layers.MaxPool2D(2,2))

model.add(layers.Conv2D(128,(3,3),activation='relu'))
model.add(layers.MaxPool2D(2,2))

#所有特征都已经特别明显了
#将所有的特征拉伸成一条直线
model.add(layers.Flatten())

#512 将拉伸的特征最后进行归纳为512个特征
model.add(layers.Dense(512,activation='relu'))

#sigmoid判断是猫是狗的概率
model.add(layers.Dense(1,activation='sigmoid'))

#配置优化器，损失函数，分类评估
#均方差：线性回归分析
#交叉熵：分类问题分析 binary_crossentropy
#metrics=['acc'] 评估分类别的成功率
model.compile(optimizer=tf.optimizers.Adam(0.001),loss='binary_crossentropy',metrics=['acc'])

# rescale=1./255 图像矩阵中0~255 缩小为0~1
train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

#train_generator 训练使用的图像容器
#validation_generator 验证使用的图像容器
#flow_from_directory 从文件夹中取出所有分类图像
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(64,64), #将所有输入的图片压缩到64x64
    batch_size=25,#每次训练都取出250张图进行训练
    class_mode='binary' #二分类
)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(64,64), #将所有输入的图片压缩到64x64
    batch_size=30,#每次训练都取出30张图进行训练
    class_mode='binary' #二分类
)

history = model.fit_generator(
    train_generator,
    steps_per_epoch=100,#train images 图片总数量 = batch_size 每次读取的图像数量 * steps 读取的次数#  < 25000  / 25 = 1000
    epochs=20,# 训练册数
    validation_data=validation_generator,
    validation_steps=22,#validation images 图片总数量 = batch_size 每次读取的图像数量 * steps 读取的次数# < 660 / 30 = 22
    verbose=2
)

import matplotlib.pyplot as plt

loss = history.history['loss'] #训练时候的损失函数（平时考试）
acc = history.history['acc'] #训练时候数据预测准确度 越接近1，证明准确性很高

val_loss = history.history['val_loss'] #验证的时候的损失函数（期末考试）
val_acc = history.history['val_acc'] #验证时候数据预测准确度 越接近1，证明准确性很高

epochs = range(len(loss)) #作为上述所有参数的横坐标

# o : 点
# - : 线
# -- : 虚线
# r、b、g 都是颜色

# 损失率的趋势图
plt.plot(epochs,loss,'r-')
plt.plot(epochs,val_loss,'b-')
plt.title('loss and val_loss')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()

# 准确率的趋势图
plt.plot(epochs,acc,'r-')
plt.plot(epochs,val_acc,'b-')
plt.title('acc and val_acc')
plt.xlabel('epochs')
plt.ylabel('acc')
plt.show()

#保存训练模型结果到本地
model.save('dog_cat.h5')





