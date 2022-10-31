# 直接定义字典
msg = {'张三':'北京朝阳','李四':'贵州安顺','王五':'云南怒江'}
a = {1:'张三',2:"李四",3:"王五"}
b = ['张三',"李四","王五"]

# 字典 各个键值对的集合
print(msg['张三'])
print(a[1])
print(b[0])
print(msg.get('张三'))

# 元组 --> 列表
a1 = (1,2,3)
a2 = list(a1)
print(a2)

# 列表 --> 字典
a3 = [1,2,3] #键列表
a4 = ['张三','李四','王五'] #值列表
a5 = dict(zip(a3,a4))
print(a5)

# 删除字典
# del msg

#清空字典
# msg.clear()
print(msg)

#修改字典
msg['张三'] = '山西太原'
print(msg)

#删除字典中的元素
del msg['张三']
print(msg)
