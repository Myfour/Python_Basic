# 函数名其实就是一个指向函数对象的引用
import math

# 定义一个函数
# 求绝对值


def my_abs(x):
    if (x < 0):
        x = -x
    return x


print(my_abs(-200))

# 如果没有return语句，函数执行后返回None


# 空函数,pass语句什么都不做，相当于一个占位符
def nop():
    pass


# 数据类型检查用内置函数isinstance()实现
x = 'haha'
if not isinstance(x, (int, float)):
    print('Not a int or a float.')

# 函数返回多个值,其实是返回了一个tuple，多个变量可以同时接收一个tuple


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)


# 函数的参数
# 位置参数
def power(x):
    return x * x


print(power(2))


# 默认参数,设置默认参数需要注意必选参数放到前面,可选的默认参数放到最后;给指定的参数传参需要表明参数名称;定义默认参数时必须指向一个不变的对象，否则参数指向的可变对象的引用会被改变
def power2(x, n=2):
    s = 1
    for item in range(n):
        s = s * x
    return s


print(power2(3, 3))
print(power2(3))


def getInfo(x, y, city='kmc', size='L'):
    print(x, y, city, size)


getInfo('jack', 'anci')
getInfo('halo', 'momo', size='M')


def add_end(L=[]):
    L.append('END')
    return L


print(add_end())
print(add_end())

# 可变参数,方法参数前加*使其变为一个可变参数；调用方法是实参list前加*使其作为一个可变参数传入


def add(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


print(add(1, 4, 5, 2, 3))
l2 = [1, 4, 5, 2, 3]
print(add(*l2))


# 关键字参数,会将**的参数封装成一个dict;调用函数时在dict前加**也可将其传入关键字参数中
def person(name, age, **kw):
    print('name:', name, ',age:', age, ',other:', kw)


person('Zack', 20, sex='男', height=190)
kw = {'size': 'L', 'hair': 'green'}
person('Zoro', 19, **kw)


# 命名关键字参数,指定关键字参数前需要加*
def person1(name, age, *, size, sex):
    print(name, age, size, sex)


person1('show', 20, sex='nv', size='XL')


# 参数中有可变参数也有命名关键字参数就不用额外加一个*
def person2(name, age, *girls, size, number):
    print(name, age, girls, size, number)


person2('heihei', 30, 'li', 'zi', 'jian', size='XXL', number='9096')


# 终极组合参数
def f1(a, b, c=0, *d, **e):
    print(a, b, c, d, e)


f1('aa', 'bb', 3, 3, 'd', kw1='xx', k2='gg')


def f2(a, b, c=2, *, size, **kw):
    print(a, b, c, size, kw)


f2(111, 222, 333, k2='k2', k3='k3', size='XXXL')
kw = {'k2': 'k2', 'k3': 'k3'}
f2(111, 222, 333, size="xxl", **kw)
