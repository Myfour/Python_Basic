# 列表生成式 最左边放要生成的列表值，之后接数据值的来源for循环，之后还可以接if判断
print([x * x for x in range(1, 11)])

print([x * 2 for x in range(1, 11) if x % 2 != 0])
# 练习
L = ['Hello', 'World', 18, None, 'aPple']
print([x.lower() for x in L if isinstance(x, str)])
