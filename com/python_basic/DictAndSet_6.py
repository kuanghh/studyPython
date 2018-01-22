# 使用 dict 和 set

# dict  Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
# dict内部存放的顺序和key放入的顺序是没有关系的。
# 创建一个 key为名字，value为分数的dict
d = {'Tom': 86, 'Mike': 95, 'Jerry': 30}

# 一、获取Tom的分数
print(d['Tom'])  # 输出  86

# 由于一个key只能对应一个value，所以，多次对一个key放入value，后面的值会把前面的值冲掉：

# 二、是通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value：
print(d.get('Tom'))   # 输出 86
print(d.get('Hello'))  # 输出 None

# 要删除一个key-value  可以通过pop(）方法
print(d.pop('Tom'))   # 输出 86
print(d)              # 输出 {'Mike': 95, 'Jerry': 30}

# 和list比较，dict有以下几个特点：
#       查找和插入的速度极快，不会随着key的增加而变慢；
#       需要占用大量的内存，内存浪费多。

# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key


# --------------------------------------------------------------------------------------

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

# 创建一个set，需要一个list集合
s = set([1, 2, 3])   # 可以简写问 s = {1, 2, 3}

# 所以它可以用来过滤掉重复的数据
s1 = set([1, 2, 3, 1])
print(s1)   # 输出 {1, 2, 3}

# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s1.add(4)
print(s1)   # 输出 {1, 2, 3, 4}

# 通过remove(key) 方法移除指定元素
s1.remove(2)
print(s1)   # 输出 {1, 3, 4}

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = {1, 2, 3}
s2 = {2, 3, 4}
print(s1 & s2)  # 输出 {2, 3}
print(s1 | s2)  # 输出 {1, 2, 3, 4}
















