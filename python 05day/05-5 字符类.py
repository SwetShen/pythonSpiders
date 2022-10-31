import re

#[字符1字符2字符3...] 可以匹配[]中的任意字符
s1 = '1x2'
r1 = '\d[+-x÷]\d'
z1 = re.search(r1,s1)
print(z1)

# [0-9] 数字
# [a-z] 小写字母 [A-Z] 大写字母

pwd = 'AbC123'
#密码的前三位是任意的大小写字母
r2 = '^[a-zA-Z]{3}'
z2 = re.search(r2,pwd)
print(z2)

#[\u4e00-\u9fa5] 匹配汉字
# \u400 => unicode 编码写法

con = 'abc'
r3 = '[\u4e00-\u9fa5]*'
z3 = re.search(r3,con)
print(z3)

