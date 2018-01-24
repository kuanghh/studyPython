# 使用 __slots__

# 可以任意帮实例绑定任何属性与方法：
class Student(object):
    pass


s = Student()
s.name = 'Mike'

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age

from types import MethodType

s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
s.set_age(20)
print(s.age)  # 输出 20


# 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s1 = Student()
# s1.set_age(20)  # 报错

# 可以给类绑定方法
Student.set_age = set_age
s1.set_age(20)
print(s1.age)  # 输出 20

# ----------------------------------------------------------------------

# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Animal实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Animal(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称


a = Animal()
a.name = 'Tom'
a.age = 5
# a.score = 95  # 报错 AttributeError: 'Animal' object has no attribute 'score'

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。

class Cat(Animal):
    pass


c = Cat()
c.score = 95  # 没问题

class Dog(Animal):
    __slots__ = ('address', 'speed')


dog = Dog()
dog.name = "Mike"
dog.age = 7
# dog.what = 89  # 报错
















