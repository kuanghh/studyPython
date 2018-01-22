# 装饰器

# 现在有一个函数,输出一个日期
def now():
    print('2018-01-22')


# 函数拥有自己的名字
print(now.__name__)  # 输出 now

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，
# 但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print("call %s():" % func.__name__)
        return func(*args, **kw)
    return wrapper

# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now2():
    print('2018-01-22')

now2()
# 输出
# call now2():
# 2018-01-22

# 把@log放到now2()函数的定义处，相当于执行了语句：
# now = log(now)


# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。

# 如果decorator本身需要传入参数,那就需要编写一个返回decorator的高阶函数,比如，要自定义log的文本：
def newlog(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


@newlog('execute')
def now3():
    print('2018-01-23')


now3()
# 输出
# execute now3():
# 2018-01-23