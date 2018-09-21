# 动态的给一个类绑定一个方法
class Student(object):
    name = None


def set_score(self, score):
    self.__score = score


def get_score(self):
    return self.__score


Student.set_score = set_score
Student.get_score = get_score
s1 = Student()
s1.set_score(15)
print(s1.get_score())
print(dir(s1))

# 由于动态绑定，为了限制实例可以绑定的属性，使用__slots__变量

print('--------------------')


class Person(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


p1 = Person()
p1.name = 'Nifer'
p1.age = '22'
print('--------------')

# p1.sex = 'man' # 这里将会报错
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：


# @property
# @property 相当于一个getter方法，用于封装一个属性的getter方法，只不过这个getter方法的名字就是属性名
# 使用了这个装饰器后就会生成一个setter方法的装饰器，@xxx.setter
# 最简单的定义一个描述符的方式就是使用@property
class AClass(object):
    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, group):
        if isinstance(group, int):
            self.__group = group
        else:
            raise ValueError('group must be an integer')

    @property
    def birth(self):
        return self.__birth

    def setBirth(self, birth):
        self.__birth = birth

    # @birth.setter
    # def birth(self, birth):
    #     self.__birth = birth


a1 = AClass()
a1.group = 100
print(a1.group)
# a1.group = 'g' # 此处会报ValueError
print(a1._AClass__group)
a1.setBirth(3.4)
print(a1.birth)

# 由于需要使用@property才能产生@xxx.setter
# 所以没法设置只写属性，但可以设置只读属性

# python支持多继承；Java可不支持，只能单继承，但可以多个实现
# class Dog(Animal,RunableMixIn,EatableMixin)
# MixIn这种设计，就是混合多种类的功能到一个类中；有点类似与java实现多个接口

# 类似__slots__ __len__ 这样的属性或函数都是具有特殊功能的
# 通过此我们可以定制类
# __str__() 用来定义print()一个对象的时候的操作
print('---------------------')


class TestStr():
    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return 'TestStr object:(%s)' % self.__name


ts1 = TestStr('mytest')
print(ts1)

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现
# 一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭
# 代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

print("-----------------------")


class Fib(object):
    def __init__(self, a, b):
        self.__a = a
        self.__b = b

    def __iter__(self):
        return self

    def __next__(self):
        self.__a, self.__b = self.__b, self.__a + self.__b
        if self.__b > 100:
            raise StopIteration()
        return self.__a

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


fib = Fib(0, 1)
for x in fib:
    print(x)
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
print('-------------------')
print(fib[4])

# 要想正确实现一个__getitem__()需要很多操作的～

# 我们知道当访问类中一个不存在的属性时会报错，其实是当查找这个不存在的属性时，若找不到就执行__getattr__(self,attr)方法
# 记住只有在找不到某个属性时才会调用这个__getattr__(self,attr)方法

print('---------------------')


class TestAttr(object):
    def __getattr__(self, attr):
        print('we are finding %s' % attr)


ta = TestAttr()
ta.a