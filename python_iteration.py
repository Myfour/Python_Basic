# 迭代,所有可迭代对象都能用for in来迭代
for x in 'asdvegs':
    print(x)
print('=====================')
# 迭代dict的key
for x in {'a': 1, 'b': 2, 'c': 3}:
    print(x)
print('=====================')
# 迭代dict的value
for x in {'a': 1, 'b': 2, 'c': 3}.values():
    print(x)
print('=====================')
# 迭代dict的key和value
for k, v in {'a': 1, 'b': 2, 'c': 3}.items():
    print(k, v)
print('=====================')


# 得到一个list中的最大最小值
def minAndMax(L):
    max, min = L[0], L[0]
    for item in L:
        if max < item:
            max = item
        if min > item:
            min = item
    return min, max


print(minAndMax([5, 3, 6, 9, 10, 45, 99, 23, 67, 100, 1]))
