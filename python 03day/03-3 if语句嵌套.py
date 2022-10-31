
# 登录
# 1、if语句嵌套必须符合逻辑层级关系（先有后有）
# 2、if语句的Tab的层级格式一定要正确
username = 'admin'
password = '123'

if username == 'admin':
    print("用户名存在")
    if password == '123':
        print("密码正确")
    else:
        print("密码输入错误")
else:
    print("用户名不存在")


# 作业 ：输入年 月 判断这个月有多少天
#