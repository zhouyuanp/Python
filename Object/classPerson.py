#析构方法

class Person:

    def __del__(self):
        print("销毁对象{0}".format(self))

p1 = Person()
p2 = Person()

del p2  #调用
print("程序结束")
del p1 #再次调用会销毁p1
print(p1)  #p1 已经被销毁