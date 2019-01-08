#多分支选择结构 需要多个表达式 表表达式之间有逻辑关系,不能随意颠倒顺序
score = int(input("输入一个分数:"))  #比较的是数字,进行转型
grade = ""
if score<60:  #有依赖关系 不独立
    grade = "不及格"
elif score<80: #60-80之间
    grade = "良好"
elif score<90: #80-90之间
    grade = "优秀"
elif score<=100:
    grade = "good"
else:             #可选的上述没有合适的之后才执行
    grade = "请输入0-100之间的数"
print("分数是{0},等级是{1}".format(score,grade)) #0和1表示占位符

#没有依赖关系  独立
score1 = int(input("请输入一个分数 :"))
grade1 = ""
if(score1<60):
    grade1 = "不及格"
if(60<=score1<80):
    grade1 = "及格"
if(80<=score1<90):
    grade1 = "良好"
if(90<=score1<100):
    grade1 = "优秀"
print("分数是{0},成绩评价是{1}".format(score1,grade1))

#已知点的坐标(x,y),判断象限
x = int(input("请输入x坐标"))
y = int(input("请输入y坐标"))
a = ""
if(x==0 and y==0):
    print("原点")
elif(x==0):
    a = "y轴"
elif(y==0):
    a = "x轴"
elif(x>0 and y>0):
    print("第一象限")
elif(x<0 and y>0):
    print("第二象限")
elif(x<0 and y<0):
    print("第三象限")
else:
    print("第四象限")


