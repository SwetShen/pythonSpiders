#方式1：直接生成所有字符的列表
import random

# numbers = ['1','2','3','4','5','6','7','8','9','0']
# lower_letters = ['a','b','c','d','e','f','g','h','i','j','k','l',
#            'm','n','o','p','q','r','s','t','u','v','w','x',
#            'y','z']
#
# upper_letters = []
# for item in lower_letters:
#     upper_letters.append(item.upper())
# # print(upper_letters)
#
# words = numbers + lower_letters + upper_letters
# # print(words)
#
# code = ''
# for i in range(4):
#     n = random.randint(0,len(words) - 1)
#     code += str(words[n])
# print(code)

#方式二，利用ascii码的转化方式
# 0-9 48-57
# A-Z 65-90 +32

numbers = []
uppers = []
lowers = []

for num in range(48,58):
    numbers.append(chr(num))
print(numbers)

for num in range(65,91):
    uppers.append(chr(num))
    lowers.append(chr(num + 32))
print(uppers)
print(lowers)