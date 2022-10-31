# 登记信息、查询
print('*'*10,'登记信息系统','*'*10,end="\n")
# 创建空字典
data = {}
while True:
    print('请选择：1）登记信息 2）查询 3）退出',end="\n")
    n = int(input('选择:'))
    if n == 1:
        name = input("请输入姓名:")
        number = input("请输入寝室号:")
        tel = input("请输入电话号:")
        #存
        data[name] = {'寝室号':number,'电话':tel}

        print('已存入',end="\n")
    elif n == 2:
        #查
        for key in list(data.keys()):
            print(key)
            print(data[key])
    elif n == 3:
        break
