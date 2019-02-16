# 测试私有属性和方法
#定义私有属性和方法的创建
class Employee: #定义雇员类
    __company = "转转"  #私有类变量

    def __init__(self,name,age):  #定义私有方法
        self.name = name   #公开的
        self.__age = age   #定义私有的属性
    def __work(self):  #定义私有方法
        print("好好工作,赚取取媳妇!!!!")
        print("年龄:{0}".format(self.__age))  #外部访问私有,内部可以随意使用,在类内部自己方法调自己的属性
        print(Employee.__company) #类内部访问私有类变量


e = Employee("高琪",18)  #类的外部,公开时可以直接调用
print(e.name)
#print(e.age)
print(e._Employee__age)  #外部访问私有属性  _类名__属性名或者方法名

print(dir(e))  #打印属性

#外部访问私有方法和属性
e._Employee__work()  #外部访问私有方法

#类外部调用类变量
print(Employee._Employee__company)

