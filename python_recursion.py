# 阶乘的递归函数
def fact(n):
    if (n == 1):
        return 1
    return n * fact(n - 1)


print(fact(3))


# 递归需要注意防止栈溢出，需使用尾递归来解决；尾递归即函数最后返回函数本身
# 汉诺塔规则：三个柱子ABC最左边A上有N个盘子，一次只能移动一个盘子
# 盘子从小到大从上到下依次摆放，移动时也要保持这个规则，如何实现从A移动所有盘子到C
def move(n, start, buffer, end):
    if (n == 1):
        print(start, '--->', end)
    else:
        move(n - 1, start, end, buffer)
        move(1, start, buffer, end)
        move(n - 1, buffer, start, end)


move(3, 'a', 'b', 'c')
