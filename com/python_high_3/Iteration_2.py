# 迭代
from collections import Iterable
# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

dic = {'Mike': 25, 'Tom': 24, 'Candy': 21, 'Cherry': 20}

for x in dic:
    print(x)
# 输出 Mike
#      Tom
#      Candy
#      Cherry
# 遍历dict，默认把所有key遍历出来


# 遍历value
for x in dic.values():
    print(x)
# 输出 25
#      24
#      21
#      20


# 同时迭代 key，value
for x, y in dic.items():
    print(x, y)
# 输出 Mike 25
#      Tom 24
#      Candy 21
#      Cherry 20


# 当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型。
# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
# 首先要 导入 from collections import Iterable
print(isinstance('abc', Iterable))      # 输出True
print(isinstance([1, 2, 3], Iterable))  # 输出True
print(isinstance(123, Iterable))        # 输出False


# 如何实现for循环里可以有下标，就例如像java的 for(int i = 0;i < size; i++)
for i, value in enumerate(['Mike', 'Tom', 'Candy']):
    print(i+1, value)
# 输出 1 Mike
#      2 Tom
#      3 Candy

