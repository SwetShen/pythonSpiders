# python的变量定义不需要定义它的所属类型
# python是一门解释型语言

Admin = 1
admin = 2
_admin = 3 #在区域中作为受保护（能访问、不能修改）的变量
__admin = 4 #在区域中作为不被访问（不能访问、不能修改）的变量
number11 = 11
my_code = 12

name = '张三'

# 解析型语言只有在解释之后才能运行。
print(admin) # 在代码使用的过程中，变量类型就会展示出来
print(name)