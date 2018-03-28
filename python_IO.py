'''
读写文件前，我们先必须了解一下，在磁盘上读写文件的功能都是由操作系统提供的，
现代操作系统不允许普通的程序直接操作磁盘，所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符），
然后，通过操作系统提供的接口从这个文件对象中读取数据（读文件），或者把数据写入这个文件对象（写文件）
'''
# 读取文件，使用open（）函数，传入文件名与标识符
file1 = open('/home/nifer/Documents/pythonIO.txt', 'r')
# 如果出现异常会报错出来，若读取文件成功，使用read（）可以将内容以str类型读取出来到内存中
print(file1.read())
# 由于打开一个文件占用操作系统的资源等一系列问题，所以一定要关闭文件,调用close（）方法
file1.close()
# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    file2 = open('/home/nifer/Documents/pythonIO.txt', 'r')
except BaseException as e:
    print('读取file2出问题了')
finally:
    # 判断一个变量是否定义 'xxx' in dir()
    if 'file2' in dir():  # 由于如果没读取到文件，file2为一个未定义的变量，无法执行close（），所以先判断是否定义
        file2.close()
    else:
        print('file2 not exists')

print('--------------------------------')
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：功能同上
with open('/home/nifer/Documents/pythonIO.txt', 'r') as file3:
    print(file3.read())
print('----------------------------')
# 文件对象的read（）方法会一次读出所有内容到内存，如果文件过大，内存会爆的，此时通过调用read（size）的单参数的方法
# 来控制每次读取的字节大小
with open('/home/nifer/Documents/pythonIO.txt', 'r') as file4:
    while True:
        buffer = file4.read(5)
        print(buffer)
        if not buffer:
            break
print('----------------------------')
# 可以直接用 with ... as ...生成的可迭代对象 利用for in来输出，系统会自动处理缓冲与内存
with open('/home/nifer/Documents/pythonIO.txt', 'r') as file5:
    for x in file5:
        print(x)
# 读取二进制文件
# 打开文件的模式选择用rb模式
print('----------------------------')
with open('/home/nifer/Pictures/Wallpapers/tt.jpg', 'rb') as file6:
    with open('/home/nifer/Pictures/a.jpg', 'wb') as file7:
        for x in file6:
            file7.write(x)
# 打开一个非UTF-8编码的文件，需要传入encoding参数
# 例如打开一个gbk编码的文件
# f=open('/s/s/s.js',mode='r',encoding='gbk')