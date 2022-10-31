
# 欢迎语句
print('-'*10,'欢迎使用ATM','-'*10)
money = 1200
status = True
# 1、查询，2、取钱，3、存钱，4、退出
while status:
    print('-'*3,'1、查询，2、取钱，3、存钱，4、退出','-'*3)
    number = int(input("请选择:"))
    if number == 1:
        print("您目前的余额:",money)
    elif number == 2:
        get = int(input("请输入取款金额:"))
        money -= get
    elif number == 3:
        save = int(input("请输入存款金额:"))
        money += save
    elif number == 4:
        status = False
        print("成功退出")
