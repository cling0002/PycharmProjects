'''
跳过
1直接跳过  @unittest.skip('跳过的原因')
2.判断条件跳过    @unittest.skipIf( condition,reason)
'''

import unittest

version=29

class TestDemo(unittest.TestCase):
    @unittest.skip('我就要跳')
    def test_1(self):
        print("测试方法1")

    @unittest.skipIf(version>=30, "版本号大于30不执行")
    def test_2(self):
        print("测试方法2")

    def test_3(self):
        print("测试方法3")
