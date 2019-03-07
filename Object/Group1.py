
#测试has-a关系,使用组合

class MobilePhone:
    def __init__(self,cpu,screen):  #初始化一个方法
        self.cpu = cpu
        self.screen = screen    #通过属性来指向对象


class CPU:
    def calculate(self):
        print("8核CPU")
        print("cpu对象：",self)

class Screen:
    def show(self):
        print("显示一个好看的画面，以后不想再为money纠结")
        print("screen对象：",self)


m = MobilePhone(CPU(),Screen())
m.cpu.calculate()
m.screen.show()













