#测试lambda 表达的式 匿名函数
f = lambda a,b,c: a*b*c # 创建一个对象,把对象的应用赋一个值

def test0 (a,b,c):
    return  a*b*c

f(1,2,3)  #直接调用
print(f(1,2,3))  #直接调用并打印返回值

print(test0(1,2,3))

#花扩号中的每一个元素都是lambda 表达式

g = [lambda a :a*2,lambda b : b*3,lambda c : c*4]
print(g[0](2))

h = [test0,test0]  #函数也是对象
h[0](3,3,3)
print(h[0](3,3,3))



