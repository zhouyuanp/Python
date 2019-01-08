#01
#num = input("输入一个数字:")
#if int(num)<10:  #转型
#    print(num)
#02 True 打印 false不打印
b = []
if not b :
    print("空列表是false,不打印结果")
#03 可以打印
c = True
if c:
    print("c")
#04 空字符串 不打印转为false
c1 = ""
if c1:
    print("c1"+"321")
#05 非空字符串
c2 = "True"
if c2:
    print("c2"+"123")
#06 测试数字 是0false 大于0是true
d = 20
if d:
    print("d"+"0 是false不打印,其他反之")
#07 测试连续判断
d1 = 3
if 4<d1<100:
    print("d1"+"测试连续判断的区间 true打印")
#测试赋值操作符 = 和运算符 ==
if 3 < d and(d==20): #3 小于d 且d等于20
    print("条件式中不能有赋值操作符 =")


