
#移舟泊烟渚,日暮客愁新.野旷天低树,江清月近人
a = [
    ['移','舟','泊','烟','渚'],
    ['日','暮','客','愁','新'],
    ['野','旷','天','低','树'],
    ['江','清','月','近','人']
]
# 横向古诗
for i in a:
    for j in i:
        print(j,end="")
    print("",end="\n")

# 纵向古诗
b = list(reversed(a))
print(b)

for i in range(0,len(a[0])):
    for j in b:
        print(j[i],end="")
    print("",end="\n")
