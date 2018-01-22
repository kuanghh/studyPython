# 使用list和tuple

# Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。

# 比如 班里的的学生可以组成一个list
student = ['Tom', 'Candy', 'Mike']

# 使用len 函数可以返回list的长度
print(len(student))

# 获取list的第一个元素
print(student[0])   # 输出 Tom

# 获取list的最后一个元素
print(student[-1])  # 输出 Mike

# 获取list的倒数第二个元素
print(student[-2])  # 输出 Candy

# 可以往list后面追加元素
student.append('Coco')
print(student)      # 输出 ['Tom', 'Candy', 'Mike', 'Coco']

# 可以将元素插入到指定的位置
student.insert(1, 'Jerry')
print(student)      # 输出 ['Tom', 'Jerry', 'Candy', 'Mike', 'Coco']

# 要删除list末尾的元素
print(student.pop())  # 输出 Coco
print(student)        # 输出 ['Tom', 'Jerry', 'Candy', 'Mike']

# 要删除指定位置的元素
print(student.pop(1))  # 输出 Jerry
print(student)         # 输出 ['Tom', 'Candy', 'Mike']

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
student[0] = 'NiKo'
print(student)        # 输出 ['NiKo', 'Candy', 'Mike']

# list里面也可以放不同的元素
L = ['hello', 123, True]
print(L)              # 输出 ['hello', 123, True]

# list 里面放list
L_2 = ['hello', [1, 2], True]
print(L_2)            # 输出 ['hello', [1, 2], True]
print(L_2[1][1])      # 输出 2

# ---------------------------------------------------------------------------------------------------

# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改，比如同样是列出同学的名字：

student_tuple = ("Tome", "Cherry", "Mike")
print(student_tuple)  # 输出 ('Tome', 'Cherry', 'Mike')

# tuple 没有 append ，没有 insert，一旦初始化，就不能改变

# 如果要定义一个空的tuple，可以写成()：
t = ()
print(t)  # 输出()

# 要定义一个只有1个元素的tuple，如果你这么定义： t = (1)，print(1) 只会输出 1 而不是输出(1)
# 这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
# 所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
t = (1,)
print(t)        # 输出(1,)
print(t[0])     # 输出(1,)
# print(t[1])     报错


# 虽然tuple不可变， 但是可以灵活的让tuple可变起来

t = (1, 2, [3, 4])
print(t)   # 输出 (1, 2, [3, 4])
# t里面有三个元素，在tuple里面，第三个元素指向了一个list，虽说 tuple是不变的，但是不变指的是“指向”不变，也就是t的第三个元素永远指向那个list，
# 但list 里面的元素是可以改变的
t[2][1] = 3.5
print(t)  # 输出  (1, 2, [3, 3.5])





