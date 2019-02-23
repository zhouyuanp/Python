# 测试重写Object的__str__() 方法

class Zhuan:  #默认继承object类

    def __init__(self,name):  # 重写 object 中的 init方法
        self.name = name

    def __str__(self):  #重写 object 中的str 方法
        return "名字是:{0}".format(self.name)


z = Zhuan("转转")
print(z)
print(dir(Zhuan))
