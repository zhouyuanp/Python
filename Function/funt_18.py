#测试 nonlocal 和global 关键字的用法

a = 100

def outer():
    b = 10
    def inner():    #现在只能调用 不能修改
        nonlocal b #声明外部函数的局部变量
        print("inner :",b)
        b = 20   #重新定义赋值
        print("inner :",b)   #重新定义后的赋值

        global a  #引用全局变量
        a = 10000  #对全局变量进行重新赋值
    inner()
    print("outer :",b)

outer()
print("a : ",a)