# JSON
# python内置的json模块提供了非常完善的Python对象到JSON格式的转换
import json
d = {'FirstName': 'Nifer', 'LastName': 'Pitou'}
# json.dumps(obj)方法将一个对象转换为标准的json字符串
d_j = json.dumps(d)
print(d)
print(type(d))
print(d_j)
print(type(d_j))
print('------------上面把dict到一个json的str的转换--------------')
# 将json字符串转换为python对象
j_str = '{"aaa":1,"bbb":2}'
print(json.loads(j_str))
print(type(json.loads(j_str)))
print('----------上面把一个json的str转换为一个dict----------------')


# 多数时候我们需要将一个class对象转成Json格式的字符串
# 1定义一个类
class Person(object):
    def __init__(self, name, age, sex):
        self.__name = name
        self.__age = age
        self.__sex = sex

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSex(self):
        return self.__sex


p1 = Person('Calina', 19, 'nv')


# 2编写类的转换函数class-->dict
def person2Dict(person):
    return dict(
        name=person.getName(), age=person.getAge(), sex=person.getSex())


# 3dumps方法的default参数用来设置对象转dict的函数,注意此处传入的是这个函数的对象引用
s_json = json.dumps(p1, default=person2Dict)
print(s_json)
print(type(s_json))
print('----------讲一个类对象转为一个json的str----------------')
# 通常一个类对象都有一个__dict__属性，这个属性就是一个dict
print(p1.__dict__)
print('-----------上面演示一个类对象的__dict__属性---------------')


# 将Json字符串转为一个对象
# 1编写dict转对象的函数
def dict2Person(d):
    return Person(d['name'], d['age'], d['sex'])


dd = '{"name": "Tina", "age": 30, "sex": "nv"}'

# 2 loads()方法的object_hook参数接收讲dict转对象的函数
print(json.loads(dd, object_hook=dict2Person))
print('-----------上面是讲一个json的str转为一个类对象-----------------')
# 中文转json的问题,dumps中的ensure_ascii的参数默认为True，会将中文表示为unicode编码的，设置为False就能显示中文
obj = dict(name='索隆', age=22)
print(json.dumps(obj, ensure_ascii=False))
j_str2 = '{"name":"卓洛","age":23}'
print(json.loads(j_str2))
p2 = Person('卡塔库栗', 27, '男')
print(json.dumps(p2, default=person2Dict, ensure_ascii=False))
j_str3 = '{"name":"卡库","age":30,"sex":"男"}'
print(json.loads(j_str3, object_hook=dict2Person).getName())
print('-----------上面是json中的中文问题-----------------')
