
# break 循环中止
for i in range(10):
    print(i)
    if i == 5:
        break

#案例 从0开始叠加，到哪一个数字时，和超过100
sum = 0
num = 0
while sum < 100:
    sum += num
    num += 1
print(num - 1)
print(sum)