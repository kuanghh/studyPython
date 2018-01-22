# 递归函数..............

# 计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


print(fact(5))  # 输出 120


# 使用递归函数需要注意防止栈溢出。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：

# fact(1000)  # 报错  Traceback (most recent call last):

# 在写递归的时候，推荐尾递归

def fact2(n):
    return fact2_iter(n, 1)


def fact2_iter(n, num):
    if n == 1:
        return num
    return fact2_iter(n - 1, num * n)


print(fact2(5))  # 输出 120


