class loginpage:
    def __init__(self, username, passdword, code):
        self.username=username
        self.password=passdword
        self.code=code
        self.button='登陆'

    def login(self):
        print(f'输入用户名{self.username}')
        print(f'password{self.password}')
        print(f'code{self.code}')
        print(f'buton{self.button}')

log=loginpage('admin','123456','6789')
log.login()

print("------------------------------------------------------")

class student:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def eat(self):
        print(f'{self.name}要吃饭')

    def sleep(self):
        print(f'{self.name}要睡觉')

    def year(self):
        self.age+=1

    def __str__(self):
        return f'姓名:{self.name},年龄{self.age}'

ming=student('小明',18)
ming.year()
ming.eat()
ming.sleep()
print(ming)
hong=student('小红',17)
hong.year()
print(hong)
print("------------------------------------------------------")
class comnputer:
    def __init__(self, brand, price):
        self.brand=brand
        self.price=price

    def play_movice(self,movie):
        print(f'{self.brand}播放电影{movie}')

mi=comnputer('小米',4999)
mi.play_movice("葫芦娃")
mac=comnputer('苹果',10999)
mac.play_movice('红楼梦')











