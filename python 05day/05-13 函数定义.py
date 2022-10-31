# 函数
# 函数是从上往下顺序执行。

#函数的定义
def fun():
    print("Hello")
#使用函数
fun()

# a,b 是fun的形参
def fun(a,b):
    print(a + b)
fun(1,2)

a = 1
def fun1(a):
    a += 1
    print('内部变量',a)
# 值传递：只存在赋值关系
fun1(a)
print('外部变量',a)

b = [1,2,3]
def fun2(b):
    b[0] = 4
    print('内部变量',b)
# 地址传递（引用传递）
fun2(b)
print('外部变量',b)

# 函数实现BMI指数
def bmi(height,weight):
    b = weight / height**2
    if b <= 18:
        print('偏瘦')
    elif 18 < b <24:
        print('正常')
    else:
        print('胖')
bmi(1.75,70)

# 函数设计，实现单一功能，代码耦合。
