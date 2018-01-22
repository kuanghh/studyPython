# 函数的参数

# 1.位置参数
# 定义一个函数，返回参数的平方值
def power(x):
    return x * x


# 其中 参数x 就是位置参数

# 2.默认参数
# 定义一个函数，其中x 为底数，n为幂，求x的n次方，如果用户没有输入n值，
# 那么可以定义一个默认参数 n=1给它
def power(x, n=1):
    su = 1
    while n > 0:
        su = su * x
        n = n - 1
    return su


# 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按照顺序，但需要指定名字,例如：
def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll("Mike", "M", city='Nanjing')


# 默认参数也会有一个坑，例如:
def add_end(L=[]):
    L.append("End")
    return L


print(add_end([1, 2, 3]))  # 输出 [1,2,3,'End']  没问题
print(add_end([1, 2, 3]))  # 输出 [1,2,3,'End']  没问题
print(add_end())  # 输出 ['End']        没问题
print(add_end())  # 输出 ['End','End']  有问题...


# 原因解释 Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以注意：定义默认参数要牢记一点：默认参数必须指向不变对象！


# 3.可变参数 :就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
def cal(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum


print(cal(1, 2, 3))  # 输出 6
print(cal(1, 2, 3, 4, 5))  # 输出 15
# 定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。
# 在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：

# 如果已经有了一个list，怎么去调用 具有可变参数的函数呢
# Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
l = [1, 2, 3, 4]
print(cal(*l))  # 输出 10


# 4.关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。请看示例：
def person(name, age, **kw):
    print('name:', name, ' age:', age, ' other:', kw)


# 可以指传指定参数
person('Mike', 39)  # 输出 name: Mike  age: 39  other: {}
# 也可以传入任意个数的关键参数
person('Tom', 30, city='Beijing', food='rice')  # 输出 name: Tom  age: 30  other: {'city': 'Beijing', 'food': 'rice'}

# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，
# 但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，
# 其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 将 dict转换成关键字传入进去
d1={'city': 'Beijing', 'job': 'Coder'}
person('Xiaoming', 10, **d1)  # 输出 name: Xiaoming  age: 10  other: {'city': 'Beijing', 'job': 'Coder'}

# --------------------------------------------------------------------------------------------------------------------

# 5.命名关键字参数
# 运用关键字参数的话，有一个缺陷，就是并不能限制传入的参数
# 举个栗子，def person(name, age, **kw)想限制传入的关键字参数只有city和job的话,可以像下面那么做
def person2(name, age, *, city, job):
    print(name, age, city, job)


# 和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person2('Mike', 20, city='Beijing', job='coder')  # 输出 Mike 20 Beijing coder
# print(person2('Mike', 20))                             # 报错，没有填写 city 还有job的参数

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了
def person3(name, age, *args, city, job):
    print(name, age, args, city, job)


# 命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
# print(person3('Jack', 24, 'Beijing', 'Engineer'))      # 报错
person3('Mike', 20, 2, 3, city='Beijing', job='coder')  # Mike 20 (2, 3) Beijing coder
person3('Mike', 20, 3, city='Beijing', job='coder')  # Mike 20 (3,) Beijing coder

# 命名关键字参数可以有缺省值，从而简化调用：
def person4(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person4('Jack', 24, job='Engineer')  # 输出 Jack 24 Beijing Engineer


# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2)
# a = 1 b = 2 c = 0 args = () kw = {}
f1(1, 2, c=3)
# a = 1 b = 2 c = 3 args = () kw = {}
f1(1, 2, 3, 'a', 'b')
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
f1(1, 2, 3, 'a', 'b', x=99)
# a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
f2(1, 2, d=99, ext=None)
# a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}
