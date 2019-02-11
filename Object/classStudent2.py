class Student2:  #注意英文符号 type 类是模具类 类对象  classStudent2 是模板类

    def __init__(self,name,score):

        self.name = name
        self.score = score
    def say_score(self):

        print("{0}的分数是：{1}".format(self.name,self.score))

stu2 =Student2

s1 = Student2("ASDFAS",80)
s2 = stu2("asdfas",100)   #s1和s2 是同样的调用

s1.say_score()
s2.say_score()