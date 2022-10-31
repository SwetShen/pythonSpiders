# 访问限制  _：受保护的(在其他的python的文件中不可以使用这个变量)
# __:不被访问的

class Test:
    a = 1
    _b = 2
    __c = 3

test = Test()
print(test.a)
print(test._b)
# print(test.__c) # __c不可以被外部访问

