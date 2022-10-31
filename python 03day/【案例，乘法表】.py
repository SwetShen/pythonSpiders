
# 1 - 9
# 行
for i in range(1,10):
    #列
   for j in range(1,i + 1):
       print(j,'x',i,'=',i * j,end="\t")
   print("",end="\n")