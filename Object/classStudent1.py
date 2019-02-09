#测试构造方法
class Student1:
    def __init__(self,name,score):

        self.name = name
        self.score = score
    def say_score(self):  #方法也是属性
        print("{0}的分数是：{1}".format(self.name,self.score))

s2 = Student1("张三",18)
s2.say_score()

s2.age = 30
s2.salary = 3000  #新增的实例属性
print(s2.salary)


s1 = Student1("zyp",18)  #新增的实例属性，s1中调用不了
s1.say_score()







