import re

pattern = r'[?|&]'

url = 'https://www.microsoft.com/login.jsp?user="xm"&pwd="xm"'
# 通过正则分割字符串
result = re.split(pattern,url)

print(result)