
class Test:
    def __init__(self):
        print("这是init的初始化方法")

# t 是Test类的对象
# __init__ 会在类创建对象时自动执行
t = Test()


class Circle:
    # 类的属性
    r = 0
    def __init__(self,r):
        print(r)
        self.r = r
    def getRound(self):
        print(2 * 3.14 * self.r)
c = Circle(8)
c.getRound()
# __init__ 可以帮助类初始化属性。

#【人的类，通过init初始化姓名年龄。对照Circle的案例】