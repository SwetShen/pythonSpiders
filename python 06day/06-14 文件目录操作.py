# 文件IO （文件输入输出）

#1、open("相对路径位置")
#2、mode文件打开模式 r 可读 w 可读可写 a+ 追加内容
file = open("pack/Test.py",mode='r',encoding='utf-8')

#3、read 读取里面的内容
print(file.read())

#4、操作完成后file文件需要关闭
file.close()

#5、通过with访问和操作文件
with open("pack/Test.py",mode='r',encoding='utf-8') as file:
    #6、read中的参数是数值，可以限制读取内容的大小
    print(file.read(20))
    file.close() 