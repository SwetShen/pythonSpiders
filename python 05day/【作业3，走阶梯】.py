
# 递归方式 ： 函数使用函数本身
# 递归 通常比三重循环需要更多内存资源，因此在程序中不推荐设计递归.
# LeeCode

def walk(n):
  if n == 1: # f(1)
      return 1
  elif n == 2: #f(2)
      return 2
  elif n > 2:
      # return f(n - 1) + f(n - 2)
      return walk(n - 1) + walk(n - 2)

print(walk(4))