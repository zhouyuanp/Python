#测试mro()
class A:
    def aa(self):
        print("aa")

    def say(self):
        print("say  AAA.....")

class B:
    def bb(self):
        print("bb")

    def say(self):
        print("say BBB.....")

class C(B,A): #寻找方法是"从左到右" # C(A,B) 此时会寻找A的
    def cc(self):
        print("cc")

c = C()
print(C.mro())   #打印类的层次结构
c.say()   #解释器寻找方法是"从左到右"的方式寻找,此时会执行B中的say()