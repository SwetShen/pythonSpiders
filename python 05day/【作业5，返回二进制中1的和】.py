
#如何把一个数据从十进制转化为二进制。

n = {'count':0}

def getBinary(num,n):
    if num < 2:
        print(num,end=" ")
        if num == 1:
            n['count'] += 1
    else:
        print(num % 2,end=" ")
        if num % 2 == 1:
            n['count'] += 1
        getBinary(num // 2,n)

getBinary(7,n)

print(n)
