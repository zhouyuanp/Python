class Students:
    company = "zhuan"  #类属性
    count = 0  #类属性
    def __init__(self,name,score):
        self.name = name  #实例属性
        self.score = score
        Students.count = Students.count + 1
    def say_score(self):  #实例方法
        print("我的公司是：",Students.company)
        print(self.name,'的分数是：',self.score)

s1 = Students('娃哈哈',80)  #s1 是实例对象，自动调用__init__()方法
s1.say_score()
s2 = Students("ASDF",60)
s3 = Students("ADSFA",20)

print('一共创建{0}个Student对象'.format(Students.count))