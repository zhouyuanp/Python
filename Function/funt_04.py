#测试函数也是对象  函数是对象可以当参数传递和返回值返回
def test01():
    print("zhuanzhuan")
test01()   #小括号就就是调用的意思   在堆创建了一次,在调用的时候可以调用多次
c = test01    #赋值也可以直接调用
c()
#栈的id
print(id(test01))
print(id(c))
print(type(c))
print(type(test01))