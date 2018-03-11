# 生成一个list列表
person = ['Angelina', 'Mikay', 'Jony J', 'GAI']
print(person)
# len函数获取list长度
print(len(person))
# 用索引来访问list中的任意元素
print(person[0])
print(person[3])
# list的索引还可以倒着用从尾部来索引
print(person[-4])
print(person[-1])
# list是一个可变有序列表，可在末尾追加元素、在任意位置添加元素、删除末尾元素，或任意位置元素、替换list任意位置的元素
person.append('yubao')
person.insert(0, 'myfour')
print(person)
person.pop()
print(person)
person.pop(2)
print(person)
person[0] = 'BestMyfour'
print(person)
