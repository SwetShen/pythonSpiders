

# print("执行代码01")
# n = 1/0 # 异常产生会中止代码的执行
# print("执行代码02")


# print("执行代码01")
# #try 尝试去执行带有异常的代码
# try:
#     n = 1/0 # 异常代码
# #except 如果在try中代码有异常，则执行它的内容，如果没有则跳过它执行
# except ZeroDivisionError as e:
#     print("异常代码处理")
# print("执行代码02")


# print("执行代码01")
# try:
#     n = 1/1
# except ZeroDivisionError as e:
#     print("异常代码处理")
# else: #在没有异常产生时，执行else内容
#     print("else 代码内容")
# print("执行代码02")


print("执行代码01")
try:
    n = 1/1
except ZeroDivisionError as e:
    print("异常代码处理")
finally:
    # 无论有没有异常都要执行
    print("finally的代码")
print("执行代码02")