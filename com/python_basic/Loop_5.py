# 循环

# 计算 1 - 10 整数之和
a = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    a += x
print(a)  # 输出 55


# 简单一点的写法，可以用range()函数 创建一个整数序列
a = 0
for x in range(10):
    a += x
print(a)  # 输出45 因为 range(x)是创建一个 小于x的整数序列，比如rang(3) 创建的序列是 [0,1,2]

# 可以通过 list(range(x)) 将range出来的序列转换成一个list
print(list(range(10)))  # 输出 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# 使用while 循环计算出 100 以内的基数之和
a = 0
n = 99
while n > 0:
    a = a + n
    n = n - 2
print(a)


# break 与 continue的用法 略











