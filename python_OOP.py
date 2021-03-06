# 类和实例


class Student(object):
    pass


print(Student)

# class后面紧接类名，类名通常大写字母开头，（object）表示这个类继承自那个类 ，所有类都继承自object
# 创建一个类的实例
s1 = Student()
print(s1)
# at 0x.......是指对象的内存地址

# 可以自由的给一个对象绑定属性
s1.name = 'Niferpitou'
print(s1.name)

print('-----------------')


# 类的初始化方法 __init__
# __init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，
# 因为self就指向创建的实例本身。
# 要定义一个类的方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，
# 除了self不用传递，其他参数正常传入：
class Me(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score

    def getScore(self):
        return self.__score

    def setScore(self, score):
        self.__score = score

    def print_score(self):
        print(self.name, '-', self.__score)

    def get_grade(self):
        if self.__score < 60:
            print('D')
        elif self.__score < 80:
            print('B')
        elif self.__score < 95:
            print('A')
        else:
            print('s')


m1 = Me('Levi', 99)
m1.print_score()
m1.get_grade()

# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，
# 虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：
# 为了保护类内部属性，在属性前加双下划线__可使这个属性变为私有的
print('--------------------')
m1.name = 'nifer'
m1.print_score()
# 若想访问 __score属性需要用相应的get set方法
print('--------------------')
print(m1.getScore())
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器
# 对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
print(m1._Me__score)

print('-------------------------')


# 继承与多态
class Animal(object):
    def run(self):
        print('Animal is running......')

    def say(self):
        print('Animal is say')


class Dog(Animal):
    def run(self):
        print('Dog is running......')


class Cat(Animal):
    def say(self):
        print('Cat is say')


class Fish(Animal):
    def run(self):
        print('Fish is runing......')

    def say(self):
        print('Fish is say')


# 俗话的鸭子类型,动态语言才有的
class DuckLike(object):
    def run(self):
        print('like a duck go')


print(Animal().run())
print(Dog().run())
print(Dog().say())
print(Cat().run())
print(Fish().run())
print(DuckLike().run())

print('------------------')

# isinstance()用来判断一个对象是否使一个类的实例
print(isinstance(Animal(), Animal))
print(isinstance(Dog(), Animal))
print(isinstance(Cat(), Animal))
print(isinstance(DuckLike(), Animal))

print('----------------------')


# 多态
def runrun(animal):
    animal.run()
    animal.run()


runrun(Animal())
runrun(Dog())
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
# 动态语言的鸭子类型特点决定了继承不像静态语言那样是必须的。

# 获取对象信息
# type()用来判断对象类型
print('--------------')
print(type(123))
print(type('sdg'))
print(type([]))
print(type(abs))
print('-----------------')
# dir()获取一个对象所有的属性与方法
# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
print(dir('abc'))
print(hasattr('abc', 'upper'))
# setattr('abc', 'y', 20)
print(getattr('abc', 'join', 100))

# 类属性
print('======================')


class Group(object):
    count = 0

    def __init__(self, name, size):
        self.__name = name
        self.__size = size


g = Group('Titan', 20)
print(Group.count)
print(g.count)
print(g._Group__name)
print(g._Group__size)
