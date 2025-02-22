import json

my_list = [{
    "name": "李华1",
    "sex": "男",
    "age": 18
}, {
    "name": "小明1",
    "sex": "男",
    "age": 16
}, {
    "name": "王五1",
    "sex": "女",
    "age": 19
}
]

with open("test.json", "w", encoding="utf-8") as f:

    json.dump(my_list,f,ensure_ascii=False,indent=3)
#ensure_ascii=False 是否显示ascii码
# indent 显示缩进