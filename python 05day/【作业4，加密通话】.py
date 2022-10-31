
# 加密方式 ：异或

con = input("输入一段话：")
# con = '曃監䫿刯'
password = int(input("输入数字密码:"))

con_en = ''
for word in con:
    # print(word)
    # 将每一个字进行ascii码转化
    word_code = ord(word)
    print(word_code)
    # 将每一个字符进行加密
    con_en += chr(word_code ^ password)
print(con_en)