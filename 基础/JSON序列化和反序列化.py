# 序列化：把python转化为json
# 反序列化： 把json转为python数据类型

import json
# data = {"name": "ly", "language": ("python", "java"), "age": 20}
# data_json = json.dumps(data, sort_keys=True)
# print(data)
# print(data_json)

class Man(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

def obj2json(obj):
    return {
        "name": obj.name,
        "age": obj.age
    }


man = Man("tom", 21)
jsonDataStr = json.dumps(man, default=lambda obj: obj.__dict__)
print(jsonDataStr)