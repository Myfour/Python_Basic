# 匿名函数
# 关键字lambda表示匿名函数

print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6])))

# :冒号前表示函数参数，之后的匿名函数体就是return的结果；匿名函数也是一个函数对象，可以将其赋值给一个变量使用

f3 = lambda x: x**3
print(f3(3))

# 匿名函数也可作为一个返回值返回


def f4(x, y):
    return lambda x, y: x + y


f5 = f4(1, 4)
print(f5)
print(f5(4, 5))
