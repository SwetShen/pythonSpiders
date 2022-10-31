
a = 1
b = 2
c = 3

# 一假即假 : and 左右的内容如果一侧为False 最终结果必为False
print( a > b and b > c) #False
print( a < b and b > c) #False
print( a < b and b < c) #True
# 一真即真 : or 左右的内容如果一侧为True 最终结果必为True
print( a > b or b > c) #False
print( a < b or b > c) #True
print( a < b or b < c) #True
# 将条件结果反置
print(not a > b ) #True
print(not a < b ) #False

#【打折活动资格判定：满900 打7折； 满600 打 8折  满300 打9折】
money = float(input("请输入价格："))

if 600 > money and money >= 300 :
    print("打9折")
if 900 > money and money >= 600 :
    print("打8折")
if money >= 900:
    print("打7折")
