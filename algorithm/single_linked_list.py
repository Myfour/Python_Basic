'''
输出单链表
'''
# 由两个list组成的单链表
listValue = [1, 5, 6, 2, 4, 3]  # 每一个元素的值
listPointer = [3, 2, -1, 5, 1, 4]  # 每个元素中指向下一个元素的地址
head = 0
print(listValue[head])
next = listPointer[head]
while next != -1:
    print(listValue[next])
    next = listPointer[next]

# 嵌套list组成的单链表
print('-------------------------------------------------')
#

linkedList = [[1, 3], [5, 2], [6, -1], [2, 5], [4, 1], [3, 4]]
value = 0
pointer = 1
head = 0
print(linkedList[head][value])
next = linkedList[head][pointer]
while next != -1:
    print(linkedList[next][value])
    next = linkedList[next][pointer]

#
print('---------------------------------------------------')
# 向单链表中添加元素
list_value = [1, 5, 6, 2, 7, 3]
list_right = [3, 2, 4, 5, -1, 1]
head = 0

prepos = 5  # 已知要插入的元素的上一个元素的位置
list_value.append(4)  # 添加一个新元素进数组
list_right.append(list_right[prepos])
list_right[prepos] = len(list_value) - 1

print(list_value)
print(list_right)
