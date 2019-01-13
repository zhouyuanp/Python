#测试全局变量 局部变量

a = 3 #全局变量

def Test01():
    b = 4 #局部变量 作用于函数内
    print(b*8)

    global a #a为全局变量的a 如果在函数内改变全局变量的值,增加关键词global 声明
    a = 300  #重新给a赋值
    print(locals()) # 打印局部变量
    print(globals())# 打印全局变量



Test01()
Test01()   #栈帧的调用一次后就会丢掉
print(a)  #a用的局部变量