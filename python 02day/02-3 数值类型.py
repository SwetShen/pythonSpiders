#整数

a1 = 10
a2 = -11
print("整数为:",a1)
print("负整数为:",a2)

# 八进制表示方式 以0o开头
a3 = 0o10
print("八进制数为:",a3)

# 十六进制表示方式 以0x开头
a4 = 0x10
print("十六进制数为:",a4)

a5 = 0o134
print(a5)
a6 = 0xea1
print(a6)
a7 = 0o2322
print(a7)
a8 = 0x4d2
print(a8)

#浮点数
b1 = 1.23
b2 = -0.34
print("浮点数：",b1)
print("负值浮点数:",b2)

#科学进制
b3 = 1.12e+3 #1.12 * 10的3次方
print(b3)
b4 = 1.12e-3 #1.12 / 10的3次方
print(b4)

# 计算身体的BMI指数。
# 体重 / 身高的平方
weight = 70 #千克
height = 1.80 #米
print(weight / (height * height))