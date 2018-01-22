# 列表生成式

# 如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：但很繁琐

# 方法二是用列表生成式
r = [x * x for x in range(1, 11)]
print(r)    # 输出 [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 还可以筛选偶数的平方
r1 = [x * x for x in range(1, 11) if x % 2 == 0]
print(r1)   # 输出 [4, 16, 36, 64, 100]

# 还可以使用两层循环，可以生成全排列：
r2 = [m + n for m in 'ABC' for n in 'ABC']
print(r2)   # 输出 'AA', 'AB', 'AC', 'BA', 'BB', 'BC', 'CA', 'CB', 'CC']



