# 已知可用for来循环的数据类型有list,tuple,dict,set,str,generator
# 这些类型的对象统称为可迭代对象
# 可迭代对象   Iterable
# 判断一个对象是不是可迭代对象
from collections import Iterable
from collections import Iterator
print(isinstance([], Iterable))  # isinstance(a,b)该方法用来判断变量a属不属于类型b
print(isinstance({}, Iterable))
print('-----------------------------')
# 既可以被for循环也可被next()的对象被成为迭代器Iterator
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance((x for x in range(3)), Iterator))
print('----------------------')
# 可迭代对象Iterable转化为迭代器Iterator，使用iter()方法即可实现从一个Iterable到Iterator的转换
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
# 可理解生成器中存储的是算法，用来计算下一个元素；其可以有无限大小的元素，但list做不到
