"""
while
Version: 0.1
Author: usrpi
date: 2020-08-23
"""

# # 作业
# # 一个班级有花名册，存在列表里面
# # 你从控制台输入一个名字，如果这个名字在花名册里面，
# # 就打印这个用户名正确，如果不存在，那就报错
# name = ['huahua', 'ta', 'tingting', 'kaka']
# username = input('请输入你的名字：')
# if username in name: # in 成员运算符
#     print('用户名正确')
# else:
#     print('用户名不正确')

# while 控制循环
# 语法：
# while 条件表达式：
    # 代码块
# 执行规律：首先判断while 后面的表达式是否成立
# 如果True 那就执行代码块，执行完毕之后，继续判断--->如果True 那就执行代码块，执行完毕之后，继续判断。。。
# 否则，不进入内部执行代码块
# 防止代码进入死循环，加一个变量来控制循环次数

# 使用while，求和1-100
sum = 0
a = 1
while a <= 100:
    # sum = sum + a
    # a = a + 1
    sum += a
    a +=1
print('1-100的和：' ,sum)

