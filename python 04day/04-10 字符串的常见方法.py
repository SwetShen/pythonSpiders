
str = '今晚我要去你家蹭吃'

#len 字符串中字符的个数
print(len(str))

# 截取对应的字符串 str[start,end,step]
print(str[3])
print(str[3:])
print(str[1:2])
print(str[3:len(str)])
print(str[:3])

#【案例，截取身份证的生日日期】
# 50010120090110444X
a = '50010120090110444X'

print(a[6:10],'年')
print(int(a[10:12]),'月')
print(a[12:14],'日')

#分割字符串 split(字符串) 以括号中的字符串为分割线，分割字符串为字符串列表
#【案例，2022/10/13】
b = '2022/10/13'
c = b.split('/')
print(c)

# 合并 合并连接的字符串.join(字符串列表)
d = ['中','国','节','日']
print('-'.join(d))

# count(字符串) 统计字符串出现的次数
msg = '好人好事，好好做事'
print(msg.count('好'))

# find（字符串）获取对应字符串的索引
print(msg.find('好'))
# find(字符串，下标)从哪个位置开始照对应字符串的索引
print(msg.find('好',1))
# find(字符串，起始下标，中止下标)从哪个位置开始照对应字符串的索引
print(msg.find('好',3,6))

# index(字符串) 与 find（字符串）相同

#startwith 判断前缀字符
s = 'www.baidu.com'
print(s.startswith('www'))

#endwith 判断后缀字符
print(s.endswith('com'))

#lower 全小写字母
print(s.lower())

#upper 全大写字母
print(s.upper())

#去掉前后空格
password = '      123  '
print(password.strip())
#lstrip 去掉左边空格  rstrip 去掉右边空格