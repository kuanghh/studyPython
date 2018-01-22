import cmath


# 定义函数

# 在Python中，定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:，然后，在缩进块中编写函数体，函数的返回值用return语句返回。

# 定义一个 求绝对值的函数
def my_abs(a):
    if a >= 0:
        return a
    else:
        return -a


print(my_abs(-99))


#  空函数:  如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
    pass


# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
# pass还可以用在其他语句里，比如：

age = 1
if age > 0:
    pass


# 让我们修改一下my_abs的定义，对参数类型做检查，只允许整数和浮点数类型的参数。数据类型检查可以用内置函数isinstance()实现：
# 参数类型检查类似与java的instanceof
def my_abs(num):
    if not isinstance(num, (int, float)):
        raise TypeError('类型出错啦')
    else:
        if num >= 0:
            return num
        else:
            return -num


print(my_abs(-100))  # 输出 100


# print(my_abs('A'))  # 输出  报错 TypeError: 类型出错啦

# ------------------------------------------------------------------------
# 返回多个值
# 在python中 可以返回多个值， 比如计算  一个 坐标
def move(xi, yi, step, angle=0):
    nx = xi + step * cmath.cos(angle)
    ny = yi - step * cmath.sin(angle)
    return nx, ny


z, w = move(100, 100, 60, cmath.pi / 6)
r = move(100, 100, 60, cmath.pi / 6)
print(z, w)  # 输出 (151.96152422706632+0j) (70+0j)
print(r)     # 输出 ((151.96152422706632+0j), (70+0j))
# 可以发现 ，当函数返回多个值时，会当成返回一个tuple！
# 但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
