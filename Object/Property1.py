#@property 装饰器的用法

class Employee:

    def __init__(self,name,salary):
        self.__name = name  #属性私有
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary
    @salary.setter #针对salary 进行设置
    def salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("输入错误,请重新输入-----  薪水范围在1000-50000这个范围")

"""  #没有使用property 的方式调用
    def get_salary(self):
        return self.__salary

    def set_salary(self,salary):
        if 1000<salary<50000:
            self.__salary = salary
        else:
            print("输入薪水错误,请重新输入.... 薪水范围在1000-50000这个范围")
"""
emp1 = Employee("转转",30000)
#print(emp1.get_salary())
#emp1.set_salary(2000)  #输入参数
#print(emp1.get_salary())

print(emp1.salary)
emp1.salary = 2000
print(emp1.salary)











