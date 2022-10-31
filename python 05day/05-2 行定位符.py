
import re
str = 'atm'

# regex = 'tm'
# result = re.search(regex,str)

# 正则表达式中的tm会默认从左往右匹配这个字符
# print(result) #None 不匹配

# $ 正则表达式的结尾
str = 'atm'
regex = 'tm$' # 此时的正则代表 以tm可以结尾
result = re.search(regex,str,re.I)
print(result)

str = 'atmd'
regex = 'tm$' #  以md结尾，无法匹配
result = re.search(regex,str,re.I)
print(result)

# # ^ 正则表达式的开头
str = 'tma'
regex = '^tm'
result = re.search(regex,str,re.I)
print(result)

str = 'atma'
regex = '^tm'
result = re.search(regex,str,re.I)
print(result)

#【案例： www开头，且com 结尾的网站】
net = 'sina.com'
regex1 = '^www'
regex2 = 'com$'
if re.search(regex1,net) != None and re.search(regex2,net) != None:
    print('正确的网站')
else:
    print('非法网站')