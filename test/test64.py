# 测试推导式  语法功能
# 测试列表推导式  方括号
y = [x*2 for x in range(1,50) if x%5==0] #列表  x属于1-49 且x/5=0
print(y)
y = []  #列表 []
for x in range(1,50):
    if x%5==0:
        y.append(x*2)  #y=x*2
print(y)
cells = [(row,col) for row in range(1,10) for col in range(1,10)] #列表
print(cells)
#字典推导式
# 字典是由key和value 组成 也可以加if  花括号
#字符串也是序列也可以遍历
#定义一个字符串
my_text = "i love you, i love sxt, i love gaoqi"
# .count 来计算这个字符(其实是每个字母出现的次数)出现的次数
#定义一个字典
char_count = {c:my_text.count(c) for c in my_text}
print(char_count)

#课下用普通循环实现上述功能

# 集合推导式 集合中没有key 只有value  集合的特点不能重复
b = {x for x in range(1,100) if x%9==0} #x 属于1-100, 并且能被9 整除  注意写法
print(b)

# 生成器推导式, 生成元组生成器可以理解为迭代器 返回一个生成器对象  一个生成器只能生成一次
gnt = (x for x in range(4))
#print(tuple(gnt))  # tuple 生成器生成元组
#print(tuple(gnt)) # 只能生成一次
#循环 遍历
#循环可以遍历列表也可以遍历可迭代的对象 生成器就是一个可迭代的对象

for x in gnt: #gnt是生成器对象,生成器是可迭代的对象 只能是使用一次
    print(x,end=",")   #只能遍历一次
print(tuple(gnt))
















