# 高阶函数
# 变量可以指向函数
# 函数名本身是一个变量
# 综上函数上通过传入函数的名称就可以将一个函数作为参数传入函数

from functools import reduce


def add(x, y, f):
    return f(x) + f(y)


print(add(-6, -5, abs))
print('-----------------------')
# Python内建了map()和reduce()函数
# map()函数接收两个参数，一个是函数一个是Iterable对象，利用传入的函数对传入的Iterable对象逐个进行相应函数操作，把结果作为一个Iterator返回

for x in map(abs, [1, 2, 4, -3, -5, -9]):
    print(x)

print('--------------------')
print(list(map(abs, [1, 2, 3, -9])))

# reduce()函数也接收两个参数，一个有两个参数的函数和一个序列，该函数做序列的累积操作


def fn(x, y):
    return x * 10 + y


print(reduce(fn, [1, 4, 7, 3]))
# 上面实际执行了 fn(fn(fn(1,4),7),3)
print('---------------------------')
# 练习
L = ['adam', 'LiSa', 'JaCK', 'gg']


def upAndDown(x):
    return x[0].upper() + x[1:].lower()


print(list(map(upAndDown, L)))

# filter()函数用于过滤序列，和map相似接收一个函数一个序列，filter会根据函数结果为true或false来决定返回的序列中保不保留值，
# true的则返回回来结果
print('---------------------')


def odd(x):
    return x % 2 != 0


n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(filter(odd, n)))

# 练习
print('---------------------------------------')


def huiwen(x):
    return x == x[::-1]


print(list(filter(huiwen, ['11111', '121', '2332', '1324', '13131'])))

# sorted()函数也是一个高阶函数，该函数可以直接对list进行排序；他还可以通过传入一个key函数来实现自定义排序，即根据
# key函数的变换结果来排序

print('------------------------')
print(sorted([4, 2, 90, 5, 12, 44]))

print(sorted([-23, -9, 2, 23, 90, -74], key=abs))
