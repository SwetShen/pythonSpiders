
a = [1,2,3]
#append(元素) 在列表中添加一个元素
a.append(4)
print(a)

# extend(列表) 列表中添加一个列表
b = [5,6]
a.extend(b)
print(a)

#  修改列表中的元素
a[0] = 0
print(a)

# 列表元素删除
del a[0]
print(a)

#根据元素值删除
a.remove(6)
print(a)

#count 统计元素出现的次数
n = a.count(3)
print(n)

#获取指定元素首次出现的下标
c = [1,2,2,1,3]
if 2 in c:
    print(c.index(2))
# print(c.index(4))
