#测试eval() 函数
eval("print('abcd')")
#第一种用法
s = "print('abcd')"
eval(s)

a = 10
b = 20
c = eval("a+b")  #代码可以从外部转入
print(c)
#第二种用法
dict1 = dict(a=100,b=200)
d = eval("a+b",dict1)
print(d)
#字典对象











