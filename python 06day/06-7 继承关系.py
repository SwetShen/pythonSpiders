
# class 子类(父类)  子类 继承 父类
# 子类拥有父类所有的“可见”内容

class Parent:
    parent_name = '父类'
    def parentRun(self):
        print('父类方法')

class Child(Parent):
    child_name = '子类'
    def childRun(self):
        print('子类的方法')

child = Child()
print(child.child_name)
child.childRun()

print(child.parent_name)
child.parentRun()

parent = Parent()
print(parent.parent_name)
parent.parentRun()