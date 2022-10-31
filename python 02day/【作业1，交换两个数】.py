a = 1
b = 2

#通过算术运算确认两者的关系
a = a - b # a保存着两个数差 -1  b依旧 2

b = b + a # b此时是之前a的值1  a保存着两个数差
a = b - a # a的值是2

print('a = ',a)
print('b = ',b)
