import numpy as np
import matplotlib.pyplot as plt
#深度学习框架
import tensorflow as tf
#keras 核心工具（隐藏层）
import keras
#layers 隐藏层
from keras import layers
#屏蔽控制所有警告
import warnings
warnings.filterwarnings('ignore')

#y = 4x + 1

#rand(1000,1) 一千行一列的随机矩阵
inputX = np.random.rand(1000,1)
correctY = 4 * inputX + 1
#加入噪点
#产生一千行一列的随机数（0~0.05）的矩阵
noise = np.random.normal(0,0.05,inputX.shape)

# print(inputX)
#y列求值
outputY = 4 * (inputX + noise) + 1 + noise
#plot 绘制坐标系图
#plot(所有x横坐标，所有y纵坐标，图的样式，图表的标题)
# plt.plot(inputX,outputY,'ro',label="XY")
# # 设置横坐标的说明
# plt.xlabel('x')
# # 设置纵坐标的说明
# plt.ylabel('y')
# # 展示出这个图表
# plt.show()

#神经网络模型
module = keras.Sequential()
#添加隐藏层
module.add(layers.Dense(8)) #第一层设置8个权值特征转化
module.add(layers.Dense(16)) #第二层设置16个权值特征转化
module.add(layers.Dense(1)) #最终有多少结果（outputY）

#SGD 优化器（设置每个层的权值）
#loss="MSE" 采用均方差损失函数评估这个模型的值
module.compile(optimizer=tf.optimizers.SGD(0.01),loss='MSE')

#训练这个模型
#validation_split 分出训练集（平时考试） 和 测试集（期末考试）
#epochs 总共训练多少次
#batch_size 每次拿出多少数据训练
module.fit(inputX,outputY,validation_split=0.25,epochs=50,batch_size=50)

'''
Epoch 1/50
5/5 [==============================] - 0s 29ms/step - loss: 6.8201 - val_loss: 3.5526

均方差 越小越好，越小越接近正确值
loss 平时成绩与正确成绩的均方差
val_loss 期末考试成绩与正确成绩的均方差

无论是测试还是验证最终均方差都呈现递减趋势，就证明训练结果良好。
'''

#使用上述的训练结果进行预测
#predict 预测
predictY = module.predict(inputX)
#展示 outputY 与 predictY 之间的差距

plt.plot(inputX,correctY,'ro',label="XY")
plt.plot(inputX,predictY,'bo',label="predict")
plt.xlabel('x')
plt.ylabel('y')
plt.show()