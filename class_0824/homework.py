"""
function
Version: 0.1
Author: usrpi
date: 2020-08-24
"""
# 1、输出直角三角形
# 循环实现
# for i in range(1,6):
#     print('*'*i)
#
# # 使用循环嵌套方式
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*', end='') # end='' 不换行
#     print('') # print语句会换行

# 2、等腰三角形 每个边都是5*
# for i in range(1,6): # 控制行数
#     for j in range(1,6-i): # 控制空格数量 i=1-->j=4 i=2-->j=3  i=3-->j=2
#         print(' ',end='' )
#     for k in range(1,i+1): # 控制*数量
#         print('* ', end='')
#     print("")

# 3、九九乘法表
# for i in range(1,10): # 控制行数
#     for j in range(1,1+i):
#         # print(str(j)+ '*'+str(i)+'='+ str(i*j)+ " ",end="") # 使用字符串拼接
#         print('%d*%d=%d ' % (j, i , i*j),end="") # 格式化输出
#         # print()
#     print('')

# 4、冒泡排序：利用for循环，完成a=[1,7,4,89,34,2]的冒泡排序
# 相邻的两个元素 依次比较
a=[1,7,4,89,34,2]  # 冒泡排序，一般最多比较n-1次
for i in range(1,len(a)-1):
    for j in range(0,len(a)-1):
        if a[j]> a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
    print(a)

print(a)