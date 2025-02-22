class house():
    def __init__(self,name,area):
        self.name=name
        self.total_area=area
        self.free_area=area
        self.item_list=[]

    def __str__(self):
        return f'户型：{self.name}，总面积{self.total_area},剩余面积{self.free_area}'f"家具名称列表：{self.item_list}"

    def additem(self,item):
         if self.free_area>item.area:
            self.item_list.append(item.name)
            self.free_area -=item.area
            print("添加成功")
         else:
            print("添加失败")


class item():
    def __init__(self,name,area):
        self.name=name  
        self.area=area

    def __str__(self):
        return f"家具名{self.name},面积{self.area}"

bed=item('xiemngsi',4)
chest=item('yigui',2)
table=item('canszhuo',1.2)
print(bed)
print(chest)
print(table)

house1=house("三室一厅",100)
house1.additem(bed)
print(house1)