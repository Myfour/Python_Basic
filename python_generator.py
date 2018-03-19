# 普通的一个列表生成式，由于内存的限制，列表容量过大会出问题；而生成器不会一次性创建所有元素，他会边循环边计算后面的元素
# 最简单的创建生成器的方法是将列表生成式的[]换为()
L = [x * x for x in range(10)]
print(L)

G = (x * x for x in range(10))
print(G)
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# print(next(G))
# 至此超出索引会报错
# print(next(G))
# 生成器是可迭代对象，所以应该使用for循环来迭代
for x in G:
    print(x)

print('--------------------下面是斐波那契数列----------------------------')

# 斐波拉契数列用列表生成式是没法写出来的
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


for x in fib(5):
    print(x)

print('--------------下面是杨辉三角-----------')

# 杨辉三角


def yhtri(height):
    lt = [1]
    for x in range(height):
        yield lt
        lt = [1] + [lt[i] + lt[i + 1] for i in range(len(lt) - 1)] + [1]


for x in yhtri(10):
    print(x)
