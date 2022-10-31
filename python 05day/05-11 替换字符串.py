import re
#re.sub(pattern,repl,string,count,flags)

str = '''
admin user
apple school
admin water
admin
'''
# re.sub(正则,替换的内容，整个字符串，数量，re.I)
regx = 'admin'
result = re.sub(regx,'user',str)
print(result)

#【案例，提取日期重要内容】
test = '''
<view>
  <block>2020-10-7</block>
  <block>2020-10-8</block>
  <block>2020-10-9</block>
  <block>2020-10-10</block>
  <block>2020-10-11</block>
  <block>2020-10-12</block>
</view>
'''

regx = '[0-9]{4}-[0-9]{2}-[0-9]{1,2}'
match = re.findall(regx,test,re.I)
print(match)

regx = '[0-9]{4}'
result = re.sub(regx,'2022',test,2,re.I)
print(result)










