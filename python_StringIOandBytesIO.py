# StringIO 只能用来操作str
from io import StringIO
from io import BytesIO
# 创建一个StringIO的对象
f = StringIO()
# 往StringIO对象中写入数据
f.write('Niferpitou')
print(f.write(' here'))
f.write(' is')
# 用getvalue（）方法可以读取整个StringIO对象中写入的str
print(f.getvalue())
# 读取StringIO
s = StringIO('hello!\nhi!\nGoodBye!')
# 第一种方式
# while True:
#     buffer = s.read(8)
#     if not buffer:
#         break
#     print(buffer)
# 第二种方式
while True:
    x = s.readline()
    if x == '':
        break
    print(x)
# 个人发现StringIO的内容被读取出来一次后该对象中就没有内容了，第二次读取就是空的，所以上述两种方法不能同时执行
# BytesIO 用来操作二进制数据

q = BytesIO()
# 此处写入的是utf-8编码后的字节
q.write('英文'.encode('utf-8'))
print(q.getvalue())

# 读取BytesIO
w = BytesIO(b'\xe8\x8b\xb1\xe6\x96\x87')
print(w.read().decode('utf-8'))
# ###########
# StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
