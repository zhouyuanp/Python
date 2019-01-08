#选择结构的嵌套 python 根据代码的缩进量来表达代码的从属关系
score = int(input("请输入一个在0-100之间的数: "))
grade = ""
if score>100 or score<0:
    print("输入错误:请输入一个在0-100之间的数") # score = int(input("输入错误:请输入一个在0-100之间的数"))
else:
    if score>=90:
        grade = "A"
    elif score >=80:
        grade = "B"
    elif score >=70:
        grade = "C"
    elif score >=60:
        grade = "D"
    else:
        grade = "E" #注意缩进来表达从属关系
    print("分数为{0},等级为{1}".format(score,grade))
print("------------------------------------------------------------")
score = int(input("请输入一个在0-100之间的数: "))
degree = "ABCDE"
num = 0
if score>100 or score<0:
    score = int(input("输入错误:请输入一个在0-100之间的数:"))
else :
    num = score//10  #score除以10取商
    if num<6:
        num=5
    print("分数是{0},等级是{1}".format(score,degree[9-num]))  #[] 商的值

