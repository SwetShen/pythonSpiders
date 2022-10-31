
with open("a.txt",mode='r',encoding='utf-8') as f:
    # print(f.read())

    # 一行一行读取内容
    # print(f.readline())
    # print(f.readline())

    # 读取所有行,将所有行内容构成一个列表
    print(f.readlines())
    f.close()