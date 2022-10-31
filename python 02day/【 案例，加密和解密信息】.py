
msg = int(input("请输入您需要加密的信息:"))
encoder = int(input("输入你信息的密码:"))

en_msg = msg ^ encoder
print("加密之后的信息：",en_msg)

dec_msg = en_msg ^ encoder
print("解密之后的信息:",dec_msg)

#【问题：输入字符'A'，对字符A加密，然后解密】
