#传递不可变对象时,不可变对象里面的包含的子对象是可变的,则方法内修改了这个可变对象原对象也发生了变化
a = 10
print("a:",id(a))

def test01(m):
    print("m:",id(m))
    m = 20
    print(m)
    print("m:",id(m))
test01(a)
#测试元组
b = (10,20,[5,6])
print("b:",id(b))

def test02(n):
    print("n:",id(n))
 #n[0] = 100   #不支持给元组赋值,因为不可变
    n[2][0] = 888 #b 列表中的第一个元素 5 变为888
    print(n)
    print("n:",id(n))

test02(b)
print(b)  #b 中5也会变化888






