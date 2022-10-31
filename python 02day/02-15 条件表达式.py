
a = 10
b = 6
r = a if a > b else b
# r 在 a > b == True 的情况下为 a 否则为b

#【判断年份是否为闰年】
# 判断条件 1、能被4整除，且不能被100 整除  1900
#         2、能被400整除
year = int(input("请输入年份："))
result = '闰年' if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0 else '平年'
print(result)