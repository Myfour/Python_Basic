# 输出
print('i am yours')
print('i\'m yours')
print('\\\t\\\n\\')
print('''
line1
    line2
line3
''')
print('a', 'b', 'c', sep=',', end='\n')

# bool值之间可以有与或非运算、and、or、not
print(True and False)
print(True or False)
print(not True)

# 空值用None表示
print(None)

# Python为动态语言
a = 37
print(a)
a = 'GG'
print(a)

# 变量在内存中的表示
a = "abc"
b = a
print(a, b, sep='/')
a = "xyz"
print(a, b, sep='/')

# 常量通常用全部大写的变量来表示,python没有一个机制来保护常量不会改变，你硬要改变也可以
PI = 3.1415926

# python中的除法
print(10 / 3)  # 精确除法，结果是浮点数
print(10 // 3)  # 地板除法，结果是整数
