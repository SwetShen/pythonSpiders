
# 面向对象特性：封装
class Test:
    a = 1
    __a = 2
    # 如果加了访问限制，则用方法完成可读可写
    def getA(self):
        return self.__a
    def setA(self,value):
        self.__a = value

# 不加访问限制，可以随意读写
test1 = Test()
print(test1.a)
test1.a = 2
print(test1.a)

# 加了访问限制，不可以随意读写
test2 = Test()
# 可读
# print(test2.__a)
print(test2.getA())
# 可写
test2.setA(8)
print(test2.getA())
