
# fun 函数定义在内存中，如果程序在执行，
# 那么函数的内存空间一直存在
# 程序执行结束后，函数就会随之销毁
def fun():
    print(123)


# lambda 当匿名函数执行完成后，就销毁
# 已知半径求周长
# lambda r:2*3.14*r 匿名函数 形参:返回值
round = lambda r:2*3.14*r
print(round(12))