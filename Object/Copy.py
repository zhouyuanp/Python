#测试对象的深拷贝和浅拷贝
import copy #导入copy 模块

class MobilePhone:
    def __init__(self,cpu,screen):  #初始化一个方法
        self.cpu = cpu
        self.screen = screen


class CPU:
    def calculate(self):
        print("8核CPU")
        print("cpu对象：",self)

class Screen:
    def show(self):
        print("显示一个好看的画面，以后不想再为money纠结")
        print("screen对象：",self)

#测试变量赋值

c1 = CPU()  #m1和m2 指的是同一个对象  地址一样
c2= c1
print(c1)
print(c2)

print("测试浅复制。。。。。")
#测试浅复制
s1 = Screen()
m1 = MobilePhone(c1,s1)
m2 = copy.copy(m1)
print(m1,m1.cpu,m1.screen)
print(m2,m2.cpu,m2.screen)

#测试深复制
print("测试深复制。。。。。")
m3 = copy.deepcopy(m1)
print(m1,m1.cpu,m1.screen)
print(m3,m3.cpu,m3.screen)














