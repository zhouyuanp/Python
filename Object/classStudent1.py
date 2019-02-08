#测试构造方法
class Student1:
    def __init__(self,name,score):

        self.name = name
        self.score = score
    def say_score(self):
        print("{0}的分数是：{1}".format(self.name,self.score))


s2 = Student1("张三",18)
s2.say_score()


