# 定制类
from types import MethodType


# 看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
#
# __slots__我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
#
# 除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。


# __str__

# 我们先定义一个Student类，然后打印它的一个实例
class Student(object):
    def __init__(self, name):
        self.name = name


print(Student("Joke"))  # <__main__.Student object at 0x0000008279597278> 输出这一堆东西， 不好看

# 此时可以重新定义__str__方法
def str(self):
    return 'name is :' + self.name


Student.__str__ = str
print(Student("Joke"))  # 输出 name is :Joke
# 但在调试的时候，依然会显示 <__main__.Student object at 0x0000008279597278>
# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
Student.__repr__ = str
s = Student("Tom")
print()

# -------------------------------------------------------------
# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 5:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值


for x in Fib():
    print(x)
# 输出 1
#      1
#      2
#      3
#      5
# -------------------------------

# __getitem__

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# Fib()[5] 报错

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 5:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


# -------------------------------------------------

# __getattr__
# 当调用实例不存在的一个属性时，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性

# ------------------------------------------------
# __call__

# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：

class Animal(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


a = Animal('HaHa')
a()  # 输出  My name is HaHa.


# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
# >>> callable(Student())
# True
# >>> callable(max)
# True
# >>> callable([1, 2, 3])
# False
# >>> callable(None)
# False
# >>> callable('str')
# False
# 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。


