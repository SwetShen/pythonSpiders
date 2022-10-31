
import re

num = 'A*B'
r2 = r'a\*b'
# re.I 不区分大小写
z2 = re.search(r2,num,re.I)
print(z2)

