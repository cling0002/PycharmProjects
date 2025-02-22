# import unittest
#
#
# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, False)  # add assertion here
#
#
# if __name__ == '__main__':
#     unittest.main()
#
#
#


'''
文件操作

open(file, mode='r', encoding=None)
file:打开的文件  类型为字符串  路径可以为相对路径和绝对路径 建议相对路径
mode：打开文件的参数    r:只读  w：写   a：追加，在文件末尾写入内容
encoding:编码方式   gbk    utf-8
返回值为一个文件对象

关闭文件：
文件对象.close()

写文件
文件对象.write('写入文件的内容')

读文件：文件打开方式为r
文件对象.read(n) 一般不写表示读取全部

文件不存在会直接创建文件
文件存在会覆盖原文件

with open()  打开文件的好处：  不要自动书写关闭文件的代码


with open(file, mode='r', encoding=None) as 变量:
    #在缩进中读取或写入文件


按行读取文件内容
文件对象.readline()
'''

'''f=open("a.txt","a",encoding='utf-8')
f.write("\n好好学习")
f.write("\n,天天向上")
f.close()'''


with open("a.txt",encoding='utf-8') as f:
    buf=f.readline()
    print(buf)
    print(f.readline())

with open("a.txt",encoding='utf-8') as f:
    for i in f:
        print(i,end='')