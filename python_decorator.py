# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('now is night')


a = now
a()
# 函数有一个__name__属性用来得到函数的名称
print(now.__name__)
print(a.__name__)

# 何为装饰器
# 假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数


def log(func):
    def wrapper(*args, **kw):
        print("call the", func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now1():
    print("now is run")


print('----------------------')
now1()
# 把@log放到now()函数的定义处，相当于执行了语句：now=log(now)

print('------------------------')


# 带参数的装饰器，相当于执行now=log(text)(now)
def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def ee():
    print('ee go')


ee()