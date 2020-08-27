"""
单元测试
Version: 0.1
Author: usrpi
date: 2020-08-27
"""

import  unittest
from  class_0827_unittest.class_01 import TestMathMethod

suite = unittest.TestSuite() # 存储用例
# 方法一：

suite.addTest(TestMathMethod('test_add_two_zero'))

# 方法二：
loader = unittest.TestLoader() # 创建一个加载器
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))
suite.addTest(loader.loadTestsFromTestCase(TestMathMethod))

# 执行
runner = unittest.TextTestRunner()
runner.run(suite)