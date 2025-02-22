'''

测试报告
1获取HTMLTestRunner
2导包unittest
3使用套件对象，加载对象，去添加用例
4是厉害第三方的运行对象，并运行套件对象


'''

import unittest




suit=unittest.defaultTestLoader.discover(".","demo06.py")
# (self, stream=sys.stdout, verbosity=1, title=None, description=None)
# stream=sys.stdout 测试报告的文件对象 （open），使用wb打开
# verbosity=1,  报告详细程度
#  title=None 测试报告标题
# description=None 测试报告描述信息


'''
from HTMLTestRunner import HTMLTestRunner
with open("report.html","wb") as f:
    runner=HTMLTestRunner(f,2)
    runner.run(suit)
    
'''

from XTestRunner import HTMLTestRunner
with open('report.html', 'wb') as fp:
    runner = HTMLTestRunner(
         stream=fp,
         title='测试报告',
         description='describe: 测测测 ',
         language='zh-CN',    #zh-CN
         rerun=3
    )
    runner.run(suit)

