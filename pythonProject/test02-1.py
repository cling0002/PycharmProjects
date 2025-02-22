# def AAA():
#     """dwawdawdwa """
#     print("hello")
#     print("world")
# AAA()
#  定义类
'''
class  类名:
    def 方法名（self）：
        pass
'''
# 创建对象
'''
变量 = 类名（） #
'''
# 调用方法
'''
对象.方法名（）
'''
class cat:
    def eat(self):
        print("chi")
        pass
    def drink(self):
        print(f'{self.name} chi')
        pass
# mao =cat()
# mao.eat()
# mao.drink()
# 添加属性
'''
对象.属性名 =属性值
在内部方法中self是对象
self.属性名 =属性值
在类中添加属性一般写在   ——init——方法中
'''
mao=cat()
mao.name='bule'

mao.drink()

'''
__init__方法
创建对象之后自动调用
用于给对象添加属性（初始化方法，构造方法）
某些代码，创建对象之后都要执行  可以将代码写在 _init_ 中


'''

class test:
    def __init__(self):
        self.name='bule'
        self.age='10'
        print("ces调用")

    def show(self):
        print(f'(name:{self.name},age:{self.age}')



'''
__str__方法
使用print打印对象的时候，自动调用
用于书写对象的属性信息  打印对象是要查看什么信息   没有定义方法 print（对象），m默认输出对象的引用地址
必须返回一个字符串 
'''

class person:
    def __init__(self, name, age):
        self.__name=name
        self.__age=age

    def __str__(self):
        return f'{self.__name},{self.__age}'

xm=person('xiaoming',18)
print(xm)
# print(xm.age)

'''
继承

class A：
    pass
    
# class B（A)：     #B类继承A类   
    pass
    
'''

class animal:
    def eat(self):
        print("吃东西")

class dog(animal):
    def bark(self):
        print("叫")

class xtq(dog):
    pass


'''ani =animal()
ani.eat()

dog=dog()
dog.eat()
dog.bark()'''

xt=xtq()
xt.eat()