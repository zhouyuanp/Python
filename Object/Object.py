#查看 继承的层次结构  mro()
class A:
    pass
class B(A):
    pass
class C(B):
    pass

print(C.mro())

#查看Object 的属性方法

class Zhuan:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def say_age(self):
        print(self.name,"的年龄是:",self.age)


obj = object()
print(dir(obj))

z = Zhuan("转转",6)  #say_age 方法也是属性
print(dir(z))


