import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras import layers
import warnings
warnings.filterwarnings('ignore')

#linspace(start,end,count) 从start开始到end的值范围内，取出1000个数
inputX = np.linspace(0.,10.,1000).reshape(1000,1)
noise = np.random.normal(0,0.05,inputX.shape)
outputY = inputX * (inputX + noise) + 1
# outputY = tf.sin(inputX + noise) + 1

# plt.plot(inputX,outputY,'ro')
# plt.title("inputX and outputY")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

#由于神经网络中只有前向传播，因此对于权重值，基本上没有任何改变，所以会呈现出直线
#activation 激活函数 （反向传播，修改权重值。）
model = keras.Sequential()
model.add(layers.Dense(8,activation="relu"))
model.add(layers.Dense(16,activation="relu"))
model.add(layers.Dense(1,activation="relu"))

#优化器
#SGD 做直线类的线性回归
#Adam 拟合各种特殊情况
model.compile(optimizer=tf.optimizers.Adam(0.001),loss='MSE')

#训练次数与训练大小不够
model.fit(inputX,outputY,batch_size=100,epochs=500,validation_split=0.25)

predictY = model.predict(inputX)

plt.plot(inputX,outputY,'ro',label="XY")
plt.plot(inputX,predictY,'bo',label="predict")
plt.xlabel('x')
plt.ylabel('y')
plt.show()