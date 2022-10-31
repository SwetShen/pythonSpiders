
#1、追加内容，不能使用w模式，因为w会删除前面所有内容
#2、追加内容，一般使用a+模式
#3、在文件未定义的情况下，a+模式会创建文件
with open("b.txt",mode="a+",encoding="utf-8") as f:
    f.write("内容")
    f.close()