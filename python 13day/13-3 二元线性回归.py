# x y z
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
import keras
from keras import layers
import warnings
warnings.filterwarnings('ignore')

inputX = np.random.rand(1000,1)
inputY = np.random.rand(1000,1)
#在多元情况下，一定要把所有的因素放置在一个矩阵中
inputXY = np.hstack((inputX,inputY))


noiseX = np.random.normal(0,0.5,inputX.shape)
noiseY = np.random.normal(0,0.5,inputY.shape)



outputZ = inputX * inputX * noiseX + inputY + noiseY + 2

#三维点图
fig = plt.figure()
#启用三维轴
ax = plt.axes(projection='3d')

# ax.plot3D(inputX.reshape(-1), inputY.reshape(-1), outputZ.reshape(-1), 'gray')
ax.scatter3D(inputX.reshape(-1), inputY.reshape(-1), outputZ.reshape(-1),
             c=outputZ.reshape(-1), cmap='Greens');

plt.show()

model = keras.Sequential()
model.add(layers.Dense(8))
model.add(layers.Dense(16))
#如果前面的因素最终只得到一个结果，则定义Dense为1
#如果前面的因素最终会得到多个结果，则定义Dense为最终分类的数量
model.add(layers.Dense(1))

model.compile(optimizer=tf.optimizers.SGD(0.001),loss='MSE')

model.fit(inputXY,outputZ,batch_size=100,epochs=500,validation_split=0.25)

predictZ = model.predict(inputXY)

fig = plt.figure()
#启用三维轴
ax = plt.axes(projection='3d')

# ax.plot3D(inputX.reshape(-1), inputY.reshape(-1), outputZ.reshape(-1), 'gray')
ax.scatter3D(inputX.reshape(-1), inputY.reshape(-1), predictZ.reshape(-1),
             c=predictZ.reshape(-1), cmap='Reds');

plt.show()




