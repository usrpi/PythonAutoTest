"""
单元测试
Version: 0.1
Author: usrpi
date: 2020-08-27
"""

# 接口测试的本质 就是测试类里面的函数
# 单元测试的本质 测试函数 代码级别 通过代码级别
# 单元测试的框架 unitest+接口 pytest+web
# pytest+jenkins+allure

# 功能测试
# 写用例-- TestCase
# 执行用例-- 1:TestSuite 存储用例  2：TestLoader 找用例，加载用例，存到1的TestSuite
# 对比实际结果 期望结果 用例是否通过———— 断言 Assert
# 测试报告   TextTestRunner

import unittest
from class_0827_unittest.math_method import MathMethod
# 写一个测试类 对我自己写的math_method模块里面的类 进行单元测试
class TestMathMethod(unittest.TestCase):# 继承unittest里面的TestCase专门来写用例
    # 编写测试用例
    # 一个用例就是一个函数 不能传参 只有self关键字
    # 所有的用例（所有的函数 都是test开头 test_）
    def test_add_two_positive(self):
        res = MathMethod(1,1).add()
        print('1+1的结果是：', res)
        self.assertEqual(2, res)

    def test_add_two_zero(self):
        res = MathMethod(0, 0).add()
        print('0+0的结果是：', res)
        self.assertEqual(0, res)

    def test_add_two_negative(self):
        res = MathMethod(-1, -2).add()
        print('-1+-2的结果是：', res)
        self.assertEqual(-3, res)

if __name__ == '__main__':
    unittest.main()
# ASCII 用例执行顺序 方法名
# test_add_two_positive  #2
# test_add_two_zero  #3
# test_add_two_negative  #1