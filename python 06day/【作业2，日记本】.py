import datetime
import os

print('*'*10,'日记本程序','*'*10,end='\n')

while True:
    print('1、写日记 2、查看所有日记 3、查看日记内容 4、退出 请选择：')
    n = int(input("输入选择数字："))
    if n == 1:
        # 输入保存日记
        txt = input("请输入日记内容：")
        t = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        with open('note/'+ t + '.txt',mode='a+',encoding='utf-8') as f:
            f.write(txt)
            f.close()
    elif n == 2:
        # 查看所有的日记
        dirs = os.listdir('note/')
        for item in dirs:
            print(item)
    elif n == 3:
        # 查询对应的日记内容
        name = input("输入日记名称:")
        with open('note/' + name + '.txt',mode='r',encoding='utf-8') as f:
            print(f.read())
            f.close()
    elif n == 4:
        break
