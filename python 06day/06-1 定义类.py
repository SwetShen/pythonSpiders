
# Test是类的名称
# name 是Test类的属性 （变量）
# walk 是Test类的行为 （功能：函数(方法)）
class Test:
    name = 'zhangsan'
    def walk(self):
        print('行走')

class Person:
    name = ''
    age = 0
    sex = '男'
    def eat(self):
        print("吃饭")
    def sleep(self):
        print("睡觉")

# 【案例,定义电脑类】
class Computer:
    logo = ''
    CPU = ''
    GPU = ''
    def playGame(self):
        print("玩游戏")
    def learn(self):
        print("学习")
    def watch(self):
        print("观影")