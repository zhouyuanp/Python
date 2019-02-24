# 测试多重继承

class A:
    def aa(self):
        print("aa")

class B:
    def bb(self):
        print("bb")
class C(B,A):   #同时继承B和A  #继承的写法  #继承后可以B和A 的所有方法
    def cc(self):
        print("cc")

c = C()
c.aa()
c.bb()
c.cc()