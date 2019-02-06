#测试对象
class Student:
    company = "zhuanzhuan"  #类属性  company公司
    count = 0 #类属性 count 计数
    def _init_(self,name,score):
        self.name = name
        self.score = score   #实例属性
        Student.count = Student.count+1

    def say_score(self):   #实例方法
        print("我的公司是：",Student.company)
        print(self.name,'的分数是：',self.score)

    say_score()
