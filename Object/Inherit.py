#测试继承的基本使用

class Person:

    def __init__(self,name,age):
        self.name = name
        self.__age = age   #私有属性


    def say_age(self):
      print("我也不知道是该坚持还是该放弃")

class Student(Person): #子类继承父类的属性和方法

    def __init__(self,name,age,score):
        Person.__init__(self,name,age)  #调用父类的构造器  #调用父类的方法  父类名.方法名(方法参数)   #继承父类的属性#必须显式的调用父类初始化方法,不然解释器不会去调用
        self.score = score

#Student-->Person--->object 类
print(Student.mro())   #打印类的继承层次


s = Student("娃哈哈",218,20)
s.say_age()
print(s.name)
#print(s.age)
print(s._Person__age)  #调用到私有属性



print(dir(s))  #查看属性
