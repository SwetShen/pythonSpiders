#安装 numpy ：pip install numpy
#使用numpy
import numpy as np

# a是一个矩阵 : 一维矩阵
a = np.array([1,2,3])
print(a)

# b 是一个二维矩阵
# print([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
print(b)

# c 将一个一维矩阵 变成二维矩阵
c = np.array([1,2,3,4,5],ndmin=2)
print(c)

# dtype 矩阵元素的类型 int float
d = np.array([1,2,3],dtype=int)
print(d)

# shape 获取矩阵的形状（几行几列）
e = np.array([[1,2],[3,4],[5,6]])
print(e.shape)

# reshape 重新设置矩阵的大小（几行几列）
# 将上述的e重置为 2行3列
e = e.reshape(2,3)
print(e)



