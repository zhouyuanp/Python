#测试嵌套函数（内部函数） 定义
def f1():
    print("f1 runing.....")
    def f2():  #定义和调用都在f1  f2隶属于f1  f2只为f1服务
        print("f2 runing.....")
    f2()   #调用

f1()
#联系内部函数 把两个函数合到一起
def printChineseName(name,familyName):
    print("{0}{1}".format(name,familyName))

def printEnglishName(name,familyName):
    print("{0}{1}".format(name,familyName))

def printName(isChinese,name,familyName):
    def inner_paint(a,b):    #定义函数
        print("{0}{1}".format(a,b))

    if isChinese:   #调用
        inner_paint(familyName,name)
    else :
        inner_paint(name,familyName)


printName(True,"元鹏","周")
printName(False,"Donald","Trump")







