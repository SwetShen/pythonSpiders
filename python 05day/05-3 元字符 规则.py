
import re

# .: 任意一个字符
str = 'abcde'

r1 = '.'
z1 = re.search(r1,str)
print(z1)

str2 = 'a'

r2 = '^.$'
z2 = re.search(r2,str2)
print(z2)

# \w 代表任意 字母 数字 下划线
r3 = '\w'
z3 = re.search(r3,str)
print(z3)

str3 = ':123'
z4 = re.search(r3,str3)
print(z4)


