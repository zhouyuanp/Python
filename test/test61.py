# 测试循环中的else语句
salarySum = 0   #薪资总和
salarys = []    #salary意思是薪资表
for i in range(4):
    s = input("请输入一共4名员工的薪资(按Q或q中途结束):")

    if s.upper()=="Q":  #大小写都能触发
        print("录入完成,退出")
        break # 中断循环
    if float(s)<0:
        continue  #继续下一次循环
    salarys.append(float(s))
    salarySum += float(s)

else:
    print("您已经全部录入完成4名员工的薪资")

print("录入薪资:",salarys)
print("平均薪资{0}".format(salarySum/4))