"""
function
Version: 0.1
Author: usrpi
date: 2020-08-23
"""


# 请把1-100的连续整数相加功能，写成一个函数

# 第一步：先用代码实现功能 还可以选取一组数据来证明自己的diamante是否正确
# 第二步：变成函数 加def
# 第三步：想办法提高代码的
def add_numbers(a,b):
    sum = 0
    for i in range(a,b+1): # 参数值不写死，提高代码复用性
        sum += i
    print(sum)
add_numbers(1,100)