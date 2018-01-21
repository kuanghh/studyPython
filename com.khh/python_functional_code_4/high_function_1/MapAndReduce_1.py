#  Python内建了map()和reduce()函数。
from functools import reduce
# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 先定义一个函数
def mySquare(x):
    return x * x


# 再定义一个Iterable对象，例如 list
l = list(range(5))

# 调用map,返回一个 Iterator 再去遍历他
newlist = map(mySquare, l)

print(list(newlist))  # 输出  [0, 1, 4, 9, 16]


# ----------------------------------------------------------

# 再看reduce

# reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，
# 其效果就是：reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 使用reduce 需要导入 from functools import reduce
def myMethod(x, y):
    return x + y


r = reduce(myMethod, [1, 2, 3])
print(r)  # 输出 6
