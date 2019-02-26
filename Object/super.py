# 测试 super()  代表父类的定义，而不是父类的对象

class A:

    def say(self):
        print("A：",self)

class B(A):

    def say(self):
        #A.say()  #只是使用A中的方法
        super().say()
        print("B：",self)


B().say()
