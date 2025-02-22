import pytest



class TestDemo2(object):     #测试类名必须以Test开头
    # def setup(self):
    #     print("开始")
    # def teardown(self):
    #     print("结束")
    # @pytest_PO.mark.run(order=1)
    def test_method1(self):
        print("测试方法2-1")

    def test_method2(self):
        print("测试方法2-2")


if __name__=='__main':
    pytest.main(['-s','test_case1.py'])
