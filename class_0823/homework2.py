"""
homework
Version: 0.1
Author: usrpi
date: 2020-08-23
"""
# 优酷笔试题
# 输入num为四位数，对其按照如下的规则进行加密：
# 1）每一位分别加5，然后分别将其替换为该数除以10取余后的结果
# 2）将该数的第一位和第四位互换
# 3）最后合起来作为加密后的整数输出


num = input("请输入四位数：")
new_num = ""
# print(type(new_num))
if len(num) == 4:
    for item in num:
        # print(type(item))
        new_num += str((int(item) + 5) % 10)
        # print(new_num)
    # 利用字符串的切片进行倒序输出
        last_str = new_num[::-1]
    print("加密后的整数为：{0}".format(last_str))
else:
    print("您输入的不是四位整数！")


