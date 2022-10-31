# 序列 ： 列表、元组、字典

# 元组是内容不可变的列表

a = ('张三','李四','王五')
b = (range(5))

print(a)
print(len(a))

# 元组没有新增 删除 修改
# a.append('赵六')
# a.remove('张三')
# a[0] = '赵六'

#删除元组
# del a

# 访问
print(a[0])
print(a[1:2])

# 什么情况下可以修改元组
# 元组中不是数值、字符串、布尔值
e = [1,2]
c = (e,[3,4])
e.append(6)

print(c)

