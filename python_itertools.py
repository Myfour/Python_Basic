import itertools
'''
    itertools中的几个无限迭代器
'''
# 1#
# naturals = itertools.count(1)  # 接受两个参数一个是起始数，一个是步长
# for x in naturals:
#     print(x)

# 2#
# cs = itertools.cycle('rapper')  # 无限循环传入的可迭代对象
# for x in cs:
#     print(x)

# 3#
# ns = itertools.repeat('12345', 4)  # 控制重复次数
# for x in ns:
#     print(x)

# 连接一组可迭代对象
ch = itertools.chain('xxx', 'fake', 'you')
for x in ch:
    print(x)