

a = ''
with open("a.txt",mode='r',encoding="utf-8") as f:
    # for i in range(20):
    #     f.write('第'+str(i)+'条信息\n')
    # f.close()
    n = 1
    while True:
        b = f.readline()
        if b != '':
            a += str(n) + '.' + b + '\n'
            n += 1
        else:
            break
    print(a)