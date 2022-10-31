
import random

import re
pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)
string = '项目名称 MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)

