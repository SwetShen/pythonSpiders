
for i in range(10):
    if i == 5:
        #执行continue会停止后面内容执行，并开始下一轮循环
        continue
    print(i)

# 计算100以内的所有的偶数和
sum = 0
for i in range(101):
    if i % 2 != 0: # 奇数都不执行相加
        continue
    sum += i
print("偶数相加的结果:",sum)
