"""
class
Version: 0.1
Author: usrpi
date: 2020-08-25
"""
# 类的语法 关键字class
# class 类名： #类名的规范是 数字字母下划线组成 不能以数字开头 首字母大写 驼峰命名
    #类属性
    #类方法

class BoyFriend:
    # 类属性
    height = 175
    weight = 130
    money = '500万'

    # 类函数
    def cooking(self): # 会做饭 
        print('男朋友要会做饭')

    def earn(self):
        print('男朋友月薪是3万')

# 实例/对象 具体的一个例子 类名()
bf = BoyFriend()
print(bf)
