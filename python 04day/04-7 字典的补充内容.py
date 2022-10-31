
shcool = {'张三':{'age':17,'addr':'北京'},'李四':{'age':18,'addr':'重庆'}}
print(shcool)

#访问张三的地址
print(shcool['张三']['addr'])

#遍历字典  key获取所有：左边的键
print(shcool.keys())
# values 获取所有：右边的值
print(shcool.values())

for key1 in list(shcool.keys()):
    print(key1)
    for key2 in list(shcool[key1].keys()):
        print(shcool[key1][key2])