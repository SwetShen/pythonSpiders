# 年份和月份判断这个月有几天
# 1、输入年份、月份
# 2、用年份判断闰年或者平年  二月
# 3、判断输入的月份是哪个月，有几天

year = int(input("请输入年份:"))
month = int(input("请输入月份:"))
day = 30

Feb = 28
#是闰年那么二月是29天
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    Feb = 29
# 31 : 1 3 5 7 8 10 12
# 30 : 4 6 9 11
if month == 4 or month == 6 or month == 9 or month == 11:
    day = 30
elif month == 2:
    day = Feb
else:
    day = 31

print("第",month,"个月有",day,"天")
