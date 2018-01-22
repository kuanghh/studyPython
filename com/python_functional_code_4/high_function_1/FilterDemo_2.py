# Python内建的filter()函数用于过滤序列。

# 和map()类似，filter()也接收一个函数和一个序列。
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素

# 过滤掉数列中为偶数的元素
def is_odd(n):
    return n % 2 != 0


print(list(filter(is_odd, list(range(23)))))  # 输出 [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]
# filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

