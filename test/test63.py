# 测试zip() 并行迭代
# 同时遍历多个字典和列表

for i in [1,2,3]:   #列表
    print(i)

names = ("高一","高二","高三","高丝")
ages = (18,16,20,26)
jobs = ("测试","开发","产品")

for name,age,job in zip(names,ages,jobs):  #序列  #循环3次 循环最少次数
    print("{0}--{1}--{2}".format(name,age,job))

#或者
for i in range(3):
    print("{0}-{1}-{2}".format(names[i],ages[i],jobs[i]))
