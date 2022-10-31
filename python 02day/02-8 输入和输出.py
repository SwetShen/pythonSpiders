
#打印  控制台输出
# print("控制台输出内容")

#控制台输入
#当运行input()函数的时候，程序会一直在”阻塞“状态（未完成运行）
# 只有在右侧输入完成时，回车确认，那么这条语句就会执行
# input("控制台输入:")

#【输入身高 体重，算出BMI指数】
# input 获取的值是一个字符串
# weight = input("请输入体重(kg):")
# height = input("请输入身高(m):")
# print("您身体的BMI指数为：",float(weight) / float(height) / float(height))

weight = float(input("请输入体重(kg):"))
height = float(input("请输入身高(m):"))
print("您身体的BMI指数为：",weight / height / height)