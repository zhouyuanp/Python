#测试组合

#测试继承实现代码的复用
class A1:

    def say_a1(self):
        print("1--1--1")

class B1(A1):

    pass

b1 = B1()
b1.say_a1()

#测试组合 同样的效果,使用组合实现代码的复用

class A2:
    def say_a2(self):
        print("2--2--2")

class B2:

    def __init__(self,a):
        self.a = a
a2 = A2()
b2 = B2(a2)    #b2.a
b2.a.say_a2()











