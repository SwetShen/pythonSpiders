import re

# 排除字符
str = '1-9'
r1 = '[^0-9]*'
z1 = re.search(r1,str)
print(z1)

# 选择字符
num = '10086'
r2 = '(10086)|(10000)'
z2 = re.search(r2,num)
print(z2)

# 身份号判定
'(^\d{15}$)|(^\d{18}$)|(^\d{17})(\d|X|x)$'