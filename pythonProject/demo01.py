class person:
    def __init__(self,name,weight):
        self.name=name
        self.weight=weight

    def __str__(self):
        return f"姓名：{self.name},体重{self.weight}"

    def run(self):
        print(f"{self.name}跑步")
        self.weight -=1


    def eat(self):
        print("吃")
        self.weight+=0.5

xiaoming=person("小明",95)
print(xiaoming)
xiaoming.run()
print(xiaoming)
xiaoming.eat()
print(xiaoming)