
# 返回值
def fun(a,b):
    # print(a + b)
    return a + b

result = fun(1,2)
print(result)

# 形参、返回值

# python的返回值可以同时返回多个值
def fun1(a,b):
    a -= 1
    b += 1
    return a,b
result = fun1(1,2)
print(result) # result 此时是一个元组

a,b = fun1(1,2) # return多个值，外部可以用多个值去获取。
print(a,b)
