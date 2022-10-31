import re

# match 从左往右匹配，如果第一个字符不匹配，则不匹配
# search 在整个字符串中查找与之匹配的字符串的第一个。

# 输入号码
tel = input("输入手机号:")
# 手机号码11位
reg1 = r'\d{11}'
isTel = re.match(reg1,tel)
if isTel != None:
    print("这是合法的电话号码")
