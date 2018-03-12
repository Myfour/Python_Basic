# 循环
# for-in
names = ['jack', 'brown', 'vice']
for item in names:
    print('hello,' + item)
# range函数可以生成一个整数序列，通过list()转换为一个list
print(range(10))
print(list(range(10)))
# while循环
x = 1
sum = 0
while x < 10:
    sum += x
    x = x + 1
print(sum)
# break语句可以提前退出循环
n = 1
while n < 10:
    if n > 5:
        break
    print(n)
    n = n + 1
# continue跳过这次循环开始下一次循环
n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
