import numpy as np

#empty 创建一个空矩阵，dtype 指定空矩阵中每一个元素会是什么类型
#dtype 指定的类型会是该类型的默认值。int float bool
x = np.empty([3,2],dtype=bool)
print(x)


# zeros 创建元素为0的矩阵
x = np.zeros(5)
print(x)

# 指定dtype 类型为整数
y = np.zeros(5,dtype=int)
print(y)

# dtype 如果前面的类型采纳不成功，就使用后一个对应的类型
y = np.zeros((2,2),dtype=[('int','int'),('bool','bool')])
print(y)

# 与zeros相同，只是默认元素为1
z = np.ones(5)
print(z)



