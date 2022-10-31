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
        data['姓名'] = name
        data['寝室'] = number
        data['电话'] = tel
        print('已存入',end="\n")
    elif n == 2:
        print('姓名:',data['姓名'])
        print('寝室:',data['寝室'])
        print('电话:',data['电话'])
    elif n == 3:
        break

# 作业： 存入多个人的信息，然后查看全部