import numpy as np

#生成4行一列
a = np.random.rand(4,1)
print(a)

#将四行一列 转化为一行四列
print(a.reshape([1,4]))

#将矩阵旋转90度
print(a.reshape(-1))

# 将多个矩阵合为一个矩阵。
inputX = np.random.rand(10,1)
inputY = np.random.rand(10,1)
inputXY = np.hstack((inputX,inputY))
print(inputXY)