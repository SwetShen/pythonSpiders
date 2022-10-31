# 数学工具类

# 排序
def sort(a):
    for j in range(len(a) - 1):
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
               tmp = a[i]
               a[i] = a[i + 1]
               a[i + 1] = tmp
    return a

def fun():
    print('fun')