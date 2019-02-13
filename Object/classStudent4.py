#测试类方法
class Student:
    company = "zhuan"    #类属性

    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod  #必须有classmethod
    def printCompany(cls): #cls 的缩写 class
        print(cls.company)
       # print(self.name)  #类方法和静态方法中不能调用实例变量和实例方法

Student.printCompany()    #调用类名.类方法名

#测试静态方法
class Student1:
    company = "zhuan"    #类属性
    @staticmethod  #定义静态方法
    def add(a,b):
        print("{0}+{1}={2}".format(a,b,(a+b)))
        return a + b

Student1.add(20,35) #静态方法调用




