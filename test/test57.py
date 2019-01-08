# 测试for循环
for x in (20,30,40):  #元组
    print(x*3,end="\t")
# 测试遍历字符串中的字符
for y in "asdfghf":   #依次向y赋值
    print(y,end="\t")
# 测试遍历字典
d = {"name":"zyp","age":26,"job":"QA"}
# 遍历key 并x和y可以重复使用
for x in d:
    print(x,end="\t")
for x in d.keys():
    print(x,end="\t")
#遍历value
for x in d.values():
    print(x,end="\t")
#遍历键值对  一个键值对当做一个元组
for x in d.items():
    print(x)

# 测试range 对象 默认步长为1
for i in range(5):
    print(i) # 遍历输出0 1 2 3 4

print("**************************")
#计算1--100 的和
sum_all = 0
for s in range(101):
    sum_all += s
print(sum_all)
#计算1--100偶数累加的和+1--100奇数累加的和
sum_all = 0
sum_odd = 0
sum_even = 0
for s in range(101):
    sum_all += s
    if s%2==1: #奇数的和
        sum_odd += s  #自增
    else:  #偶数的和
        sum_even += s #自增
print("1--100 累加的和{0},奇数的和{1},偶数的和{2}".format(sum_all,sum_odd,sum_even))







