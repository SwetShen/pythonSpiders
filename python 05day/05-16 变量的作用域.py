
# 全局变量
# a = 10

# 1、在函数内部定义的变量只能作用函数内部
# 2、在函数内部变量没有定义，则向函数外部寻找定义
def fun():
    # 局部变量
    a = 6
    print(a)

    # global + 变量 => 全局变量
    global b
    b = 17
fun()
# print(a) 局部变量不可以在外部访问
print(b)

