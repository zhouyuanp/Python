#多态

class Man:

    def eat(self):
         print("晚上回去吃,炸串....")
class Chinese(Man):
    def eat(self):
        print("中国人用筷子吃饭")

class English(Man):
    def eat(self):
        print("英国人用叉子吃饭")

class Indian(Man):
    def eat(self):
        print("印度人用手抓着吃饭")

def manEat(m):
    if isinstance(m,Man):
        m.eat()   #是Man的子类就可以  #多态 一个方法的调用 根据对象的不同,调用不同的方法
    else:
        print("不能吃太多饭,要减肥")

manEat(Man())
manEat(Chinese())
manEat(English())  #根据传的参数不用,调用不同的方法













