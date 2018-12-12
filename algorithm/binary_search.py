'''
二分查找有序数组中的元素
'''
array = [1, 3, 5, 6, 7, 8, 13, 14, 15, 17, 18, 24, 30, 43, 56]
head = 0  # 头指针指向第一个元素
tail = len(array)  # 尾指针指向最后一个元素加1
search = int(input('Enter a number you find:'))
while tail - head > 1:
    mid = (head + tail) // 2
    if search < array[mid]:
        tail = mid
    elif search > array[mid]:
        head = mid
        # head = mid + 1  # head移动到mid加1，因为原始的mid的元素已经小于search了 可以省去
    elif search == array[mid]:
        ans = mid
        break
else:
    if search == array[head]:
        ans = head
    else:
        ans = -1
print(ans)
