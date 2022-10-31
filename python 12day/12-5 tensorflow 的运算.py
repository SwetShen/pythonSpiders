import tensorflow as tf
import numpy as np

print(tf.add(1,2))
# tf.Tensor(3, shape=(), dtype=int32)
# tf.Tensor 张量（矩阵）
# shape=() 没有矩阵
# dtype=int32 数据类型是int类型32位

#矩阵a
a = np.array([[1,2],[3,4]])
#矩阵b
b = np.array([[1,1],[1,1]])
#将两个矩阵相加
print(tf.add(a,b))

# print(tf.multiply(a,b))

# c = [1,2,3] + [4,5,6]
# print(c)


#TensorFlow 的运算都是张量（矩阵）运算。