
class A:
    number = 11
    def run(self):
        print('父类的方法')

class B(A):
    number = 12
    def run(self):
        print('子类的方法')

b = B()

# 当子类中定义了与父类中相同的属性和方法，
# 那么子类对象只会执行子类中定义的内容

print(b.number)
b.run()