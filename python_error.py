'''
try:...except xxx as e:...finally:是Python的异常处理机制
Java的异常处理使用 try{}...catch(){}...finally{}
'''
import logging
try:
    print('Try.....')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('execpt:', e)
finally:
    print('finally....')
print('END')

print('-----------------')

# 错误应该有很多种类，如果发生了不同类型的错误，应该由不同的except语句块处理。没错，可以有多个except来捕获不同类型的错误：
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

print('---------------')
# python中的错误也是一个类，所有错误都继承自BaseException，所以在捕获一个错误时，会讲其子类也一并捕获了
try:
    print('try...捕获子类问题')
    a = 10 / 0
    print(a)
except BaseException as e:  # 此处由于BaseException是所有错误的父类，其已经捕获了其自身及子类，所有后续的捕获不到了
    print('BaseException catch..')
except ZeroDivisionError as e:
    print('ZeroDivisionError Catch..')
print('END')
print('---------------')
'''
记录错误
Python内置的logging模块可以很容易的记录错误信息
'''


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


main()
print('END')

print('---------------------------')


# 抛出错误
class FooError(ValueError):
    pass


def test(s):
    n = int(s)
    if n == 0:
        raise FooError('错在你输入了0')
    print(n)


test('0')