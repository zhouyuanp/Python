#测试局部变量 全局变量
import math  #导入方法
import time
def test01():
    start = time.time()  #开始时间
    for i in range(10000000):
        math.sqrt(30) #开方
    end =time.time() #结束时间
    print("耗时{0}".format((end-start)))
def test02():  #局部变量
    b = math.sqrt
    start = time.time()
    for i in range(10000000):
        b(30)
    end = time.time()
    print("耗时{0}".format((end-start)))
test01()
test02()