
grade = 80
#成绩要么及格、不及格
if grade >= 60:
    print("及格")
else: # else 这个关键词 一定会取到前面条件的相反条件
    print("不及格")

if grade >= 90:
    print("优秀")
elif grade >= 80: # elif = else if
    print("良好")
elif grade >= 70:
    print("中等")
elif grade >= 60:
    print("及格")
else:
    print("不及格")