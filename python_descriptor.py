'''
描述符
某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符
@property装饰器可以将一个成员函数变为一个描述符
'''


# 1.__dict__属性
class Test:
    cls_val = 1

    def __init__(self, *args, **kwargs):
        self.ins_val = 10


t = Test()
print(Test.__dict__)
print(t.__dict__)
print('---' * 30)
# 改变实例的类属性，只是为对象添加了这个属性，并不影响类的该属性
t.cls_val = 20
print(Test.__dict__)
print(t.__dict__)
print('---' * 30)
# 改变类的属性,实例的类属性也不会受到影响
Test.cls_val = 30
print(Test.__dict__)
print(t.__dict__)
# 综上可知类属性cls_val只属于类本身的属性，不是属于对象的属性;
# 而后对象中出现的属性只不过是同名的新增的对象的属性
print('---' * 30)

# 2.魔法方法：__get__(), __set__(), __delete__()


class Desc:  # 定义了一个类，其实这个类就是一个描述符；个人理解有点类似于一个带有getter,setter的属性
    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):  # 测试类
    x = Desc()  # 该测试类的一个属性，该属性是一个描述符，个人理解就是一个带getter，setter的属性


# 以下为测试代码
t = TestDesc()
t.x  # 当访问属性时，调用其get方法
t.x = 2  # 当为属性赋值时，调用其set方法

# 某个类，只要是内部定义了方法 __get__, __set__, __delete__ 中的一个或多个，就可以称为描述符

# Why？
print('-----' * 30, '\n')

