#嵌套循环 一个循环体内嵌套另一个循环
for x in range(5):  #控制内循环和循环内容  小循环
    for y in range(5): #控制外循环和循环次数 大循环
        print(x,end="\t")  #循环体
    print()    #起到换行的作用
for x in range(5):
    for y in range(10):
        print(x,end="\t")
    print()
#测试九九乘法表
for m in range (1,10):
    for n in range (1,m+1):
        print("{0}*{1}={2}".format(m, n, (m * n)), end="\t")
        #print(m ,"*",n ,"=",m * n ,end="\t") java写法
    print()

# 打印表格 用到列表和字典 存储表格的数据
#用字典来表示内容 dict
r1= dict(name="高小1",age=18,salary=30000,city="北京")
r2= dict(name="高小2",age=19,salary=20000,city="上海")
r3= dict(name="高小3",age=20,salary=10000,city="深圳")
#定义列表
tb = [r1,r2,r3]
#遍历列表的内容
for x in tb:
    if x.get("salary")>15000:   #判断是否大于150000.注意会调用方法
        print(x)







