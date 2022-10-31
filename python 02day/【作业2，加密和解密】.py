
password = 123
character = 'A'
#将字符转化为数值
character_ascii = ord(character)
#将数值进行加密处理
character_pwd = character_ascii ^ password
#将加密后的数值转化为字符
character_pwd_chr = chr(character_pwd)
print("加密后的内容:",character_pwd_chr)

#将加密字符转化为数值
character_pwd_ascii = ord(character_pwd_chr)
#对数值进行解密处理
character_dec = character_pwd_ascii ^ password
#获取解密后的字符内容
character_dec_chr = chr(character_dec)
print("解密之后的内容：",character_dec_chr)