import re

str = '小明的衣服上写着小明的名字'

regx = r'小明'
#将字符中匹配正则的内容输出
match = re.findall(regx,str,re.I)
print(match)

pattern = r'mr_\w+'
string = 'MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)

string = '项目名称 MR_SHOP mr_shop'
match = re.findall(pattern,string,re.I)
print(match)