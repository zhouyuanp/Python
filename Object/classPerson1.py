#测试方法的动态性
class Person:   #在类内定义方法
    def work(self):
        print("努力上班!")

def play_name(s):  #定义函数
    print("{0}在玩游戏".format(s))

def work2(s): #定义函数
    print("好好工作,努力上班! 赚大钱,娶媳妇!")

Person.play = play_name; #定义新方法

p = Person()
p.work()
p.play()   #方法的调用过程 Person.play(p)

Person.work = work2  #修改已经定义的方法
p.work()










