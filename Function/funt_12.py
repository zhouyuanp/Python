#测试可变参数处理(元组,字典 两种方式)
def f1 (a,b,*c):  #测试元组
    print(a,b,c)

f1(15,20,25,30)
def f2 (a,b,**c): #测试字典
    print(a,b,c)

f2(1,2,name = 'zyp',age = '27',said = '不要等待别人来爱自己,去积极应对爱情,不怕拒绝')

def f3(a,*b,**c):  #测试元组和字典
    print(a,b,c)

f3(1,2,3,said = '努力提升自己,只为遇到更好的她' )
#强制命名 在带*号的后面添加新的参数必须是强制命名

def f4(*a,b,c):  #调用时强制命名
    print(a,b,c)

f4(1,2,b = 5,c = 6)
def f5(*a,b,c,**d):
    print(a,b,c,d)


f5(1,2,b = 5,c = 6,name = '加油鸭',Thank = '谢谢你喜欢我',Rely = '保护她,不依赖她')  #调用时强制命名





