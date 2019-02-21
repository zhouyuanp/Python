#测试方法的重写

class Person :

    def __init__(self,name,age):
        self.name = name
        self.__age = age   #私有属性

    def say_age(self):
        print("我的年龄:",self.__age)

    def say_name(self):
        print("我的名字是{0}".format(self.name))


class Student(Person):

    def __init__(self,name,age,score):    #必须显式的调用父类初始化方法.不然解释器不会调用
        Person.__init__(self,name,age)
        self.score = score

    def say_name(self):
        """重写了父类的方法"""#功能是对父类的方法做修改
        print("你好,世界:{0}".format(self.score))



s = Student("转转",18,80)
s.say_age()
s.say_name()  #不重写时会调用父类的方法










