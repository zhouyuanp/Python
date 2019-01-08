#测试双分支
s = input("输入一个数字:")
if int(s)<10:
    print("s是小于10的数")
else:
    print("s是大于10的数")

#测试三元条件运算符   条件为真(true)的值 if  (条件表达式) else 条件为假(false)时的值
print("true s是小于10的值" if int(s)<10 else "false s 是大于10的数字")
num = input("请输入一个值:")
print(num if int(num)<10 else "输入的数字大于10")