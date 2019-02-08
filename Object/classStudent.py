#测试对象
class Student:

    #定义类名 首字母大写 驼峰式
    company = "zhuanzhuan"  #类属性  company公司
    count = 0 #类属性 count 计数
    def __init__(self,name,score): #构造方法 需要用下划线   self 是指当前对象本身 self 必须位于第一参数
        # 类名
        # 注意是双下划线
        self.name = name
        self.score = score   #实例属性
        Student.count = Student.count+1

    def say_score(self): #实例方法  self 必须位于第一参数
        print("我的公司是：",Student.company)
        print(self.name,'的分数是：',self.score)

