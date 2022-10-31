
#作业4：输入n值，打印n层“杨辉三角”
# 输入的阶数
n = 8

list = [[1],[1,1]]

for i in range(2,n):
    tmp = []
    tmp.append(1)
    for j in range(1,i):
        # 添加上一行的前两个数据之和
        tmp.append(list[i - 1][j - 1] + list[i - 1][j])
    tmp.append(1)
    list.append(tmp)

# print(list)
for array in list:
    for i in  array:
        print(i,end=" ")
    print("",end="\n")


