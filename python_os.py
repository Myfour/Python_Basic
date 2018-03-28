'''
如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令。
如果要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作
系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
'''
import os
print(os.name)  # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print('-------------------------')
print(os.uname())
# 获取更加详细的操作系统信息，注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# 环境变量
print('-------------------------')
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print('-------------------------')
print(os.environ.get('PATH'))

# 操作文件和目录
print('-------------------------')
# 查看当前的工作路径
print(os.path.abspath('.'))
# 拼接一个路径,当需要拼接路径时使用该函数的好处是他会自动处理不同操作系统之间的路径分隔符
print(os.path.join('/home/nifer', 'testdir'))
# 创建一个目录
print(os.mkdir('/home/nifer/testdir'))
# 删除一个目录
os.rmdir('/home/nifer/testdir')
# 拆分路径,这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/home/nifer'))
# 获取文件扩展名
print(os.path.splitext('/home/nifer/Pictures/a.jpg'))
# 重命名文件,linux下的重命名操作其实是一个mv命令，移动文件并且重命名
# os.rename('/home/nifer/Pictures/a.jpg', '/home/nifer/Pictures/tttt.jpg')
# 删除文件 os.remove('a.jpg')
# 得到一个文件夹列表;os.listdir('...')是用来列出该路径下的所有文件和目录，不是列出目录的;
# os.path.isdir()用来判断该路径是否是一个目录，要注意是否是绝对路径的问题；除非判断当前工作目录，可以使用相对路径
print([
    x for x in os.listdir('/home/nifer/Pictures')
    if os.path.isdir('/home/nifer/Pictures/' + x)
])
# 得到一个文件的列表
print([
    x for x in os.listdir('./Python_Basic')
    if os.path.isfile('./Python_Basic/' + x)
])
