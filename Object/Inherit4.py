# 测试特殊属性
class A:
    pass


class B:

    pass

class C(B,A):

    def __init__(self,m):
        self.m = m

    def cc(self):
        print("cc")


c = C(5)


print(c.__class__)  #查看对象所属的类 属于C类
print(c.__dict__)   #对象的属性，用字典的格式表示
print(C.__bases__)  #类的基类，用元组的形式表达，多继承
print(C.__base__)   #类的基类 只显示了B
print(C.__dict__)   #对象的属性，用字典的格式表示  属性
print(C.mro()) #类的层次结构 继承了B,A 和object
print(A.__subclasses__())  #查看有哪些类继承了A ,A的子类列表

