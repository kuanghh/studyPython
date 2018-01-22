# 类访问限制
class Student(object):

    def __init__(self, name, _score, __age, __address__):
        self.name = name
        self._score = _score
        self.__age = __age
        self.__address__ = __address__

    def get_age(self):
        return self.__age


student = Student("Jack", 85, 20, "广东省广州市")

print(student.name)         # 输出 Jack
print(student._score)       # 输出 85     # 不建议这样访问
# print(student.__age)        # 报错
print(student.__address__)  # 输出 广东省广州市    # __address__是特殊变量，所以可以直接访问


# 有些时候，你会看到以一个下划线开头的实例变量名，比如_score，这样的实例变量外部是可以访问的，

# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。
# 不能直接访问__age是因为Python解释器对外把__age变量改成了_Student__age，所以，仍然可以通过_Student__age来访问__age变量：
print(student._Student__age)  # 输出 20


# 最后注意下面的这种错误写法：
student.__age = 23
print(student.__age)   # 输出23

# 表面上看，外部代码“成功”地设置了__age变量，但实际上这个__age变量和class内部的__age变量不是一个变量！
# 内部的__age变量已经被Python解释器自动改成了_Student__age，而外部代码给student新增了一个__age变量。
print(student._Student__age)  # 输出 20
