
number = int(input("请输入一个数:"))

if number % 3 == 2 and number % 5 == 3 and number % 7 == 2:
    print("满足条件，这个数为：",number)
else:
    print("不满足条件")