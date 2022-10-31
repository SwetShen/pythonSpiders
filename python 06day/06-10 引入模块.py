
import re
#将本地的MathUtil.py文件引入

# import MathUtil
#
# a = [6,5,4,3,2,1]
# b = MathUtil.sort(a)
# print(b)

# as 别称： 对导入模块进行别称处理
# import MathUtil as mu
# a = [6,5,4,3,2,1]
# b = mu.sort(a)
# print(b)

# from 模块 import 函数1,函数2... ：从模块中引入函数
from MathUtil import sort,fun
a = [6,5,4,3,2,1]
b = sort(a)
fun()
print(b)
