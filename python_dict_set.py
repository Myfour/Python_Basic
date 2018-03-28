# dict字典使用键值对存储，在Java中类似Map;以下是两种创建dict的方式
score = {'Math': 90, 'Chinese': 80, "English": 70, "Other": "your choice"}
print(score)
another = dict(name='NiferPitou', author='Hunter')
print(another)
# 两种取到value的方式
print(score.get('English'))
print(score['Math'])
# 设置一个key value的方式
score['PUBG'] = 101
print(score)
# 判断key中有没有
print('DNF' in score)
print(score.get('DNF'))
print(score.get('DNF', -2))
# 删除一个key
print(score.pop('Other'))
print(score.pop('Other', 'Nothing Found'))
# dict是根据key的哈希算法来找到对应的value，所以key需要是一个不可变的对象，如字符串与整数，list则不可

# set无重复的元素的一个跟list很像的集合,无序无重复的集合
s = set([1, 1, 1, 2, 2, 3, 4, 5])
print(s)
# 通过add方法可往其中添加元素
s.add('hehe')
print(s)
# remove()可以删除元素
s.remove('hehe')
print(s)
# set集合可做交集、并集的操作
s2 = set([4, 5, 6])
print(s & s2)
print(s | s2)
#
t1 = (1, 2)
ss = {t1: 'a'}
print(ss)
print(ss[(1, 2)])
