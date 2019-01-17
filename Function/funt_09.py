#浅拷贝
import copy  #导入copy模块
def testCopy ():
    '''测试浅拷贝'''
a = [10,20,[5,6]]  #定义列表
b = copy.copy(a)
print("a:",a)
print("b:",b)

b.append(30) #增加30
a.append(40)
b[2].append(7) #在a的子列表表示[2]
print("浅拷贝----------")
print("a:",a)
print("b:",b)
#深拷贝 可以解释为克隆一个家庭
def testDeepCopy():
    '''测试深拷贝'''
    a = [10,20,[5,6]]
    b = copy.deepcopy(a)
    print("a:",a)
    print("b:",b)

    b.append(30)
    b[2].append(7)
    print("深拷贝------")
    print("a:",a)
    print("b:",b)



testDeepCopy()


