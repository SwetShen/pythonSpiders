# 在字符串前加上'r'表示正则表达式
import re

num = 'a*b'
r2 = r'a\*b'
z2 = re.search(r2,num)
print(z2)