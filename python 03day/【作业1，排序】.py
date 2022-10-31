#作业1：要求列表不使用sorted 完成一次从小到大的排序


#列表
a = [6,5,4,3,2,1]

#两两比较，得到最大数
for j in range(len(a) - 1):
    for i in range(len(a) - 1):
        if a[i] > a[i+1]:
            tmp = a[i]
            a[i] = a[i+1]
            a[i+1] = tmp
    print(a)
