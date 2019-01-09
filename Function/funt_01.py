#一个函数通常完成一个功能被重复的调用 函数先定义后调用
# 函数的分类  内置函数 标准库函数 第三方库函数 用户自定义函数
def test01():# 定义
    print("1"*10)  # 语句块
    print("2"*10)
#普通调用
test01()

#循环调用
for i in range(10):
    test01()

print(id(test01)) # test01 堆的地址
print(type(test01)) #test01 的类型
print(test01)  #打印的key











