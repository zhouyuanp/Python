# 测试递归函数基本原理  自己调用自己
def test01(n):
    print("test01：",n)
    if n==0:
        print("over")
    else:
        test01(n-1)    # 测试自己的调用自己有报错   想办法让程序停下来
    print("test****",n)
def test02():
    print("test02")





test01(4)