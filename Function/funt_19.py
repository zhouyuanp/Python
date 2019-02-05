#测试 LEBG 规则

#Local(内部函数)-->Enclosed(外层函数)-->Global(全部变量)-->Built in(python 内部类 class‘str’)

str = "global str  3"

def outer():
    str = "outer  2"
    def inner():
        str = "inner  1 "
        print(str)  #str2 会有保错
    inner()

outer()