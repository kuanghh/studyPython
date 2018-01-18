# 生成器

# 列表生成式如下
r = [x * x for x in range(1, 11)]

# 则 生成器如下
g = (x * x for x in range(1, 11))
# 通过next(g),可以将一个一个元素获取出来
print(next(g))  # 输出  1
print(next(g))  # 输出  4
print(next(g))  # 输出  9
print(next(g))  # 输出  16
# generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。

# 不断用next（g）是不正确的，应该使用for循环的
g2 = (x * x + x for x in range(1, 5))
for x in g2:
    print(x)


# 输出 2
#      6
#      12
#      20

# 定义 generator的第二种方法
# 举个栗子，斐波那契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(m):
    n, a, b = 0, 0, 1
    while n < m:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# fib(6)
# 输出 1
#      1
#      2
#      3
#      5
#      8

# fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
#  要把fib函数变成generator，只需要把print(b)改为yield b就可以了：
def fib_generoter(m):
    n, a, b = 0, 0, 1
    while n < m:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'done'


# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
fib_g = fib_generoter(7)
for x in fib_g:
    print(x)


# 输出 1
#      1
#      2
#      3
#      5
#      8
#      13

# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中

# 杨辉三角
def yang(num):
    j = 0
    l = [1]
    while j < num:
        yield (l)
        nl = []
        size = len(l)
        i = 0
        while i < size + 1:
            if i == 0:
                nl.append(l[i])
            elif i == size:
                nl.append(l[size - 1])
            else:
                nl.append(l[i - 1] + l[i])
            i = i + 1
        l = nl
        j = j + 1


yang_genertor = yang(10)
for x in yang_genertor:
    print(x)
