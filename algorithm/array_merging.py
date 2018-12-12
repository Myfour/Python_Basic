'''
合并有序数组
'''
array_1 = [1, 3, 4, 6, 10]
array_2 = [2, 5, 8, 11]

ans = array_1.copy()
ind = 0
for i in range(len(array_2)):
    while (ind < len(array_1)):
        if array_2[i] <= array_1[ind]:
            ans.insert(ind + i, array_2[i])
            break
        else:
            ind += 1
    else:
        ans = ans + array_2[i:]
        break
print(ans)
