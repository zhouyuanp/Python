#测试返回值
#没有返回值默认返回null 结束函数的运行 返回的结果可进行运算
#返回值功能
def add (a,b):
    print("计算两个数的和:{0},{1},{2}".format(a,b,(a+b)))
    return a+b

#结束运行功能
def test02():
    print("zyp")
    print("用心学习做好记录课后经常复习")
    return  #结束运行
    print("娃哈哈")

#测试返回多个值
#可以使用列表 元组 字典 集合 等容器将值存起来
def test03(x,y,z):
    #return [x*10,y*10,z*10]  #列表
    return{x*10,y*10,z*10}



c = add(20,30)  #可直接给c赋值进行#可直接看成一个数直接用

print(c)
print(add(30,60)*10)

a = test02()   #函数体中不包含return语句就返回None的值
print(a)

print(test03(10,20,30))

