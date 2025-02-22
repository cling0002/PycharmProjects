import json

from parameterized import parameterized
import unittest

from pythonProject.test04 import login

'''
  参数化
  1.导包
  2.定义测试类
  3.书写测试方法
  4.组织测试数据并传参
  
  测试数据的结构 [(),(),(),()]  or[{},{},{},{}]
'''
'''data = [
    ("admin", "123456", "登陆成功"),
    ("root", "123456", "登陆失败"),
    ("admin", "123123", "登陆失败")
]
'''
def build_data():
    with open("data01.json",encoding="utf-8") as f:
        res=json.load(f)
        data=[]
        for i in res:
            data.append((i.get("username"),i.get("password"),i.get("expect")))
    return data


class Testlogin(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login(self,  username, password,expect):
        self.assertEquals(expect, login(username, password))
