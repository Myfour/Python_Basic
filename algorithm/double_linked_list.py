'''
双链表
'''
# 三个list组成的双链表
right_pointer = [2, 4, 3, 1, 5, -1]
linked_list = [1, 4, 2, 3, 5, 6]
left_pointer = [-1, 3, 0, 2, 1, 4]

head = left_pointer.index(-1)
print(linked_list[head])
next = right_pointer[head]
while next != -1:
    print(linked_list[next])
    next = right_pointer[next]

#
print('----------------------')
#
# 反向输出

head = right_pointer.index(-1)
print(linked_list[head])
next = left_pointer[head]
while next != -1:
    print(linked_list[next])
    next = left_pointer[next]
