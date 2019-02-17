#测试@property的用法

class Employee:
    @property  #装饰器 关键字 #定义装饰器
    def salary(self):
        print("娃哈哈----- 加油啊 ")
        return 10000

emp1 = Employee()   #把类赋值empt1
#emp1.salary()   #普通的调用方式

print(emp1.salary)  #像调用属性一样调用  @property 的调用









