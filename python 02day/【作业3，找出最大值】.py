
a = 3
b= 4
c= 2
# 条件表达式只能判断两个值
# a 和 b 的大小
max_ab = a if a > b else b
max_ab_c = max_ab if max_ab > c else c
print("最大值",max_ab_c)

#max = (a if a > b else b) if (a if a > b else b) > c else c