#测试call可调用对象方法

class SalaryAccount:

    """计算工资"""
    def __call__(self,  salary):
        print("算工资啦-----")
        yearSalary = salary*12
        daySalary = salary//22.5 #国家规定平均每月工作日
        hourSalary = daySalary//8
        return dict(yearSalary=yearSalary,monthSalary=salary,daySalary=daySalary,hourSalary=hourSalary)   #可以返回元组，列表，字典



s = SalaryAccount()
print(s(6600))