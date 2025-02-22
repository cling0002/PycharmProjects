'''
class dog:
    count=0


    def __init__(self, name):
        self.name=name
        dog.count +=1

www=dog('笑话')

print(dog.count)

# 类方法
class demo:
    @classmethod
    def func(cls):
        pass

# 静态方法
class demo1:
    @staticmethod
    def func():
        pass
'''

import random


class game:
    top_socre=0
    def __init__(self, name):
        self.name=name
    @staticmethod
    def show_help():
        print('帮助')

    def sow_top_scor (self):
        print(game.top_socre)
 
    def start_game(self):
        a=random.randint(10,100)
        if a>=game.top_socre:
            game.top_socre=a
            print(a)
        else:
            print(a)


ga=game("王")
ga.start_game()
ga.start_game()
ga.sow_top_scor()
ga.show_help()