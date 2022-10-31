
import re

# ?代表0个和1个
s1 = 'colour'
r1 = 'colou?r' # u要么存在，u要么不存在
z1 = re.search(r1,s1)
print(z1)

# +代表1个或者多个
s2 = 'gooooooooooogle'
r2 = 'go+gle' # u要么存在，u要么不存在
z2 = re.search(r2,s2)
print(z2)

# *代表0个或者多个
s3 = 'ggle'
r3 = 'go*gle' # u要么存在，u要么不存在
z3 = re.search(r3,s3)
print(z3)

# {n}代表n个
s4 = 'google'
r4 = 'go{2}gle' # u要么存在，u要么不存在
z4 = re.search(r4,s4)
print(z4)

# {n,}代表n个及以上个数
s5 = 'google'
r5 = 'go{2,}gle' # u要么存在，u要么不存在
z5 = re.search(r5,s5)
print(z5)

# {n,m}代表n个至m个
s6 = 'google'
r6 = 'go{0,2}gle' # u要么存在，u要么不存在
z6 = re.search(r6,s6)
print(z6)