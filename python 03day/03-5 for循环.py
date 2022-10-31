
# 指定循环次数，直到结束
# 序列：列表
# for i in [0,1,2,3,4,5]:
#     print(i)

# range 函数规定序列的大小
# [0,1,2,3,4,5] == range(6)

# for i in range(6):
#     print(i)
# range函数： range(start,end,step)
# start 起始位置（包含）
# end 终点位置（不包含）
# step 步长,省略的情况下，默认为1

for i in range(10,101,2):
    print(i)

#【作业：输出100以内能够被三除尽的数】
for i in range(101):
    if i % 3 == 0:
        print(i)
