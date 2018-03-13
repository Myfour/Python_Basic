Name = ['json', 'kid', 'honda', 'zack', 'sabas']
# 切片操作,切片遵循[]左闭右开
print(Name[:3])  # :前的索引为0可省略
print(Name[1:3])
print(Name[-4:])  # 切片的索引也可以倒着来
print(Name[:-3])
print(Name[-4:-2])
# ：：后可以添加每隔几个切片
print(Name[::2])
print(Name[0:3:2])

# 字符串，元组也支持切片操作，切片结果对应相应的类型
print('sdgrgdsdioo' [5:])
print((1, 4, 2, 5, 6, 43, 23)[3:5])


# 利用切片实现一个trim()
def trim(str):
    while (str[0] == ' '):
        str = str[1:]
    while (str[-1] == ' '):
        str = str[:-1]
    return str


print(trim(' cxdsdf   '))