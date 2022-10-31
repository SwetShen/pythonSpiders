# 集合

a = {'红楼梦','水浒传','西游记','三国演义'}

# set函数中的序列，必须是字符串不重复

#列表 --> 集合
b = ['红楼梦','水浒传','西游记','三国演义','水浒传']
a1 = set(b)
print(a1)

#元组 --> 集合
c = ('红楼梦','水浒传','西游记','三国演义')
a2 = set(c)
print(a2)

#添加集合元素
a.add('活着')
print(a)

#del setname #删除整个集合
#setname.remove(element) # 移除指定元素
#setname.pop() #删除最后一个元素
#setname.clear() #清空集合