import os

print(os.getcwd()) # 获取当前目录的绝对路径
# print(os.listdir("./")) # 访问当前目录
# print(os.listdir(".")) # 访问当前目录
# print(os.listdir("D:/")) # 访问D盘下的所有文件
print(os.listdir("../")) # 返回上一级目录

# os.mkdir("os模块创建目录") # 创建指定目录
# os.makedirs("a/b") # 创建多级目录

# os.rmdir("") #删除指定目录
# os.removedirs("a/b") # 删除多级目录

# os.remove("b.txt") #删除文件
# os.rename("a.txt","b.txt") #重命名
# print(os.stat("b.txt")) # 文件的信息