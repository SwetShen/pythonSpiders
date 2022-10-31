
# re = regex 正则表达式
import re

str = 'atmd'

# match 匹配
# Match对象 = re.match(正则字符串，需要匹配的字符串)

regex = 'tm'
result = re.match(regex,str)
print(result)
# <re.Match object; span=(0, 2), match='tm'>
#  <> :对象
#  re.Match： 名为Match的对象
#  object ： 对象
#  span : 正则匹配到的字符串的位置
#  match ：匹配的字符串

print(result.span()) # 元组（0，2）
print(result.string) # string 输出原字符串
# print(result.string[result.span()[0]:result.span()[1]])
