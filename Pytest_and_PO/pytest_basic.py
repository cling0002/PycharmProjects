'''
命令行模式运行      pytest_PO -s XXX.py

主函数模式   if__name__=='__main__'
                pytest_PO.main(["-s","XXX.py"])

   函数级别执行顺序  先setup（）->测试方法 teardown（）方法


测试类
    测试类名必须以Test开头
    、

特殊方法函数级别和类级别同事使用
class TestDemo(object):
  def test_method1(self):

            print('测试函数1')
    def test_method2(self):

          print('测试函数2')

配置文件使用
    1项目下信件scripts模块
    2将测试脚本文件放到scripts中
    3pytest的配置文件放在自动化项目目录下
    4名称为pytest.ini
    5命令行运行时会使用该配置文件中的配置
    6第一行内容为【pytest_PO】

注意
    配置文件不允许使用注释
    一个工程只有一个pytest.ini
    配置有pytest 配置i文件的工程  打开命了行  输入pytest指令 即可运行

使用步骤
    默认设置

        [pytest_PO]
        testpaths=./case
        addopts=-s
        python_files=test*.py
        python_classes=Test*

html报告   --html=./Pytest_and_PO/XXX.html
控制方法    --self-contained-html        @pytest_PO.mark.run(order=2)

失败重试    --reruns 1

跳过      @pytest_PO.mark.skipif()
参数化     @pytest_PO.mark.parametrize('参数1‘,’参数n',[(数据1，数据n),(数据2，数据n),(数据3，数据n  )])


断言
    assert
'''

# def test_func():
#     '''测试函数'''
#     print('测试函数')

import pytest


class TestDemo(object):     #测试类名必须以Test开头
    def setup(self):
        print("开始")
    def teardown(self):
        print("结束")



    # '''测试演示类'''
    def test_method1(self):     #'''测试方法名必须以test开头'''
          # '''测试函数1'''
            print('测试函数1')
    def test_method2(self):
          # '''测试函数2'''
          print('测试函数2')
#         特殊方法吗写法固定，                函数级别执行顺序  先setUp（）->测试方法 teardown（）方法


if __name__=='__main':
    pytest.main(['-s','pytest_basic.py'])
