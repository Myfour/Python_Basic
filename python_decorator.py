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


def requires_int(func):
    def judge(*args, **kwargs):
        args_list = [i for i in args]
        kwargs_list = [i for i in kwargs.values()]
        for arg in args_list + kwargs_list:
            if not isinstance(arg, int):
                raise TypeError('args must be intger')
        return func(*args, **kwargs)

    return judge


@requires_int
def get(x, y, gg, qq):
    return 'This is get.....'


print(get(12, 1, 99, 100))
# print(get(gg='this is gg', x=12, y=33, qq=44))  # 上述装饰器实现判断参数必须为int类型

print('------------------------')


# 带参数的装饰器，相当于执行now=log(text)(now);带参数的装饰器实质是先用带参数的函数返回一个装饰器的引用，在内层才是真正的装饰器
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


@log('intersting')
def game():
    print('game go')


ee()
game()