
def fun1(a,b):
    print(a + b)
# fun1(1) 参数个数要正确
# fun1(1,2,3)

# c=12 当外部没有为c传值，c会按照默认值执行
def fun2(a,b,c=12):
    if a > b:
        c += 1
    print(c)
fun2(2,1)

# *args 可以接受任意长度的参数（可变长参数）
def fun2(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)
fun2(1,2,3,4)
fun2(*[1,2,3,4])

# **args 可变长的键值对
def fun3(**args):
    print(args.keys())
    print(args.values())
fun3(**{'张三':12,"李四":13})
