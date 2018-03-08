# Python字符串是以Unicode编码的
print('包含中文，繁體中文，English')

# 字符串的类型为str，在网络上传输就变为bytes，bytes类型用b前缀的单引号或双引号表示
x = b'royal'
print(x)

# str类型通过encode（）可以编码为指定的bytes
print('ab'.encode('ascii'))
print('ab'.encode('utf-8'))
print('哈哈'.encode('utf-8'))
print('哈哈'.encode('gb2312'))

# 将从网络上的bytes转换为str
print(b'gg'.decode("ascii"))
print(b'gg'.decode("utf-8"))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode("utf-8"))

# len()计算str的字符数,也可以计算bytes的字节数
print(len('ggsimida'))
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中'.encode('utf-8')))

# 字符串的格式化
# 第一种
print('this %s is %s \'s website' % ('www.myfour.org', 'myfour'))
# 第二种:字符串的format（）方法
print('this {0} is {1} \'s website'.format('www.myfour.org', 'myfour'))
