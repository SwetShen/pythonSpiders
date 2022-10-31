
# 定义列表
names = ['张三','李四','王五']

# 访问 “列表变量[下标]”  下标==索引
print(names[0])

print(names[-3])
print(names[-1]) # 访问最后一个元素，用下标-1

#切片
# list[start:end:step]
# start 开始的下标（包含）
# end 结束的下标（不包含）
# step 步长
print(names[1:3])

print(names[1:-1])

#序列相加 将多个序列拼接起来
a = [1,2,3]
b = [4,5,6]
print(a + b)

print(a + names)

#矩阵运算 Numpy Pandas: 图像处理
#图像处理: 将旧清晰处理。

#序列的乘法
print(a * 3)
#print(a * b) 原生python不支持矩阵运算

#检查元素是否存在于序列中
print('张三' in names)
print('李五' in names)

# len 计算列表的长度 (有多少元素在列表中)
print(len(names))

# max min 获取列表的最大值和最小值
print(max(a),min(a))

# str 将序列转化为字符串
print(str(names) + '是一个字符串')

# sum 计算整个序列的和
print(sum(a))

# sorted 对序列进行排序
c = [6,2,1,5,7,3]
print(sorted(c))

#reversed 让序列倒置
#reversed(c) 得到对象
#list 将对象变成列表
print(list(reversed(c)))

# 创建数值列表
d = list(range(0,10))
print(d)

# 删除列表
del d
# print(d)