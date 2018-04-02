# namedtuple
# 带有名字的元组，且该元组中获取元素的方式不再是使用索引，而是用属性来引用某个元素
# 我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
from collections import namedtuple, deque, OrderedDict, Counter
point = namedtuple('Point', ['x', 'y'])
p = point(10, 20)
print(p.x)
print(p.y)
print(isinstance(p, point))
print(isinstance(p, tuple))
# example
print('--------------------')
circle = namedtuple('Circle', ['x', 'y', 'r'])
c = circle(1, 1, 5)
print('该圆位于x:', c.x, 'y:', c.y, '半径为:', c.r)
# deque
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
print('--------------------------')
dq = deque(['q', 'w', 'e', 'r'])
print(dq)
dq.append('a')
dq.append('s')
print(dq)
# deque除了提供list所具有的方法外,还提供了appendleft（）和popleft（）
# 这样就方便了从头部添加与删除元素
dq.appendleft('d')
dq.appendleft('f')
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict：
# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
print('-----------------------------')
# od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
od = OrderedDict(a='1', b='2', c='3')
print(od)
od2 = OrderedDict()
od2['z'] = 10
od2['y'] = 9
od2['a'] = 5
print(od2.keys())
# Counter
# 一个简单的计数器
c = Counter()
for x in 'programming':
    c[x] = c[x] + 1
print(c)
