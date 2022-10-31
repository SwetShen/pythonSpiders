
class A:
    def run(self):
        print("父类 run")

    def __init__(self):
        print("父类的init方法")

class B(A):
    def run(self):
        #当子类方法中需要父类的方法执行内容
        super().run()
        print("子类 run")

    def __init__(self):
        # 当init中需要调用父类的init方法时
        # super(子类，self).__init__()
        super(B, self).__init__()
        print("子类的init方法")

b = B()
# b.run()