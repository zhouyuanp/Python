#测试continue
#要求输入员工的薪资,若薪资小于0,则重新输入,最后打印录入工的数量和薪资明细,以及平均工资
empNum = 0
salarySum = 0
salarys = []
while True :
    s = input("请输入员工的薪资(按 Q 或 q 结束):")
    if s =="q" or s=="Q":
        print("录入完成,退出")
        break
    if float(s)<0:
        continue
    empNum +=1   #员工人数加和
    salarys.append(float(s))  #数值转换浮点数
    salarySum += float(s)  #把转换后的浮点数给 salarySum  赋值   薪资加和
print("员工数{0}".format(empNum))
print("录入薪资:",salarys)
print("平均薪资{0}".format(salarySum/empNum))

